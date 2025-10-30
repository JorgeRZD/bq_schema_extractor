import json
import os
from datetime import date

#¡¡¡¡¡¡MODIFY THIS PATH TO LOCATION WHERE bq_json_schema_extract.sh SAVED FILE SCHEMA JSON FILE FROM GCP!!!!!!!
download_folder_path = "/Users/jorgeortiz/Downloads/"
#¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def view_creator(json_bq_schema_file: str, pk: str):
    opening_schema_string = '{\n    "schema": ['
    closing_schema_string_1 = f'    ],\n    "description": " ",\n    "labels": {{\n        "release_type": "np-ga",\n        "goog_terraform_provisioned": "true"\n    }},\n'
    closing_schema_string_pk = f'    "primary_key": "{pk}",\n'
    closing_schema_string_2 = f'    "use_legacy_sql": false,\n    "deletion_protection": false\n}}'

    table_folder = json_bq_schema_file.split('.')[-2].split('-')[-1]
    os.makedirs(table_folder, exist_ok=True)
    content_string = ''
    count = 0

    try:
        with open(download_folder_path + json_bq_schema_file, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: file '{json_bq_schema_file}' not found in {download_folder_path}. Make sure to input the correct file name.")
        return
    except json.JSONDecodeError:
        print(f"Error: file '{json_bq_schema_file}' is not valid JSON.")
        return

    for i in json_data:
        count += 1
        if count != len(json_data):
            content_string += f'        {{\n            "name": "{i['name']}",\n            "type": "{i['type']}",\n            "mode": "NULLABLE",\n            "description": " " \n        }}'+',\n'
        else:
            content_string += f'        {{\n            "name": "{i['name']}",\n            "type": "{i['type']}",\n            "mode": "NULLABLE",\n            "description": " " \n        }}'

    final_closing_schema_string = closing_schema_string_1+closing_schema_string_pk+closing_schema_string_2
    output_path = os.path.join(table_folder, "schema.json")
    with open(output_path, "w") as f:
        f.write(opening_schema_string + '\n' + content_string + '\n' + final_closing_schema_string)

def query_creator(json_bq_schema_file: str):
    today = date.today().strftime("%Y-%m-%d")
    columns_string = ""
    count = 0
    table_folder, dataset_name = json_bq_schema_file.split('.')[-2].split('-')[-1], json_bq_schema_file.split('.')[-2].split('-')[-2]
    select_string = "SELECT\n"
    close_string = f"\nFROM `${{life_cycle_prefix}}-supply-chain-thd.{dataset_name}.{table_folder}`;"
    header_string = f"""/*===================================================
    Create Date:   {today} Jorge Ortiz ARN8XLP
    As of Date:    {today} Jorge Ortiz ARN8XLP
    Purpose/Notes: 
    Pipeline:      
    ==================================================== */\n"""

    with open(download_folder_path+json_bq_schema_file, 'r') as json_file:
        json_data = json.load(json_file)
        for i in json_data:
            count += 1
            if count != len(json_data):
                columns_string += '\t' + i['name'] + ',\n'
            else:
                columns_string += '\t' + i['name']

    os.makedirs(table_folder, exist_ok=True)
    output_path = os.path.join(table_folder, "query.sql")

    with open(output_path, 'w') as f:
        f.write(header_string + select_string + columns_string + close_string)


def main():
    json_bq_schema_file = input("Enter the name of the JSON BQ (with .json extension): ")
    json_bq_schema_file = json_bq_schema_file.strip()
    pk = input("Enter the primary key column name (separate columns with comma if key is composite): ")
    pk = pk.strip().upper()
    view_creator(json_bq_schema_file, pk)
    print(f'+++ Creating schema.json in folder {json_bq_schema_file.split(".")[-2].split("-")[-1]} +++\n')
    query_creator(json_bq_schema_file)
    print(f'+++ Creating query.sql in folder {json_bq_schema_file.split(".")[-2].split("-")[-1]} +++\n')
    print("+"*38 + "\n" + "+++ Process completed successfully +++\n" + "+"*38) 

if __name__ == "__main__":
    main()