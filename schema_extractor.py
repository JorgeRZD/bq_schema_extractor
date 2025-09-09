def json_schema_cols_import(json_bq_schema_file: str, data_type: bool):
    """
    Extracts column names (optinally also data types) from a JSON BigQuery schema file.

    Args:
        json_bq_schema_file (str): BigQuery schema file name.
        data_type (bool): If True, returns data types in DDL format.
                          If False, returns a list of column names only.

    Returns:
        list: list of column names, or a list of names and data types separated by spaces.
    """
    import json

    cols_names = []
    download_directory_path = "F:/Descargas/"
    with open(download_directory_path + json_bq_schema_file, "r") as json_file:
        json_data = json.load(json_file)

    if data_type == False:
        for i in json_data:
            cols_names.append(i["name"])
        return cols_names

    else:
        for i in json_data:
            cols_names.append(i["name"] + " " + i["type"])
        return cols_names


def main():
    file_name = input("Enter json file with a BigQuery SQL table schema:")
    data_type_requirement = input("Is data type required? (True/False):")
    data_type_requirement = data_type_requirement.strip().lower() == "true"
    cols_names = json_schema_cols_import(file_name, data_type_requirement)
    print(",\n".join(cols_names))


if __name__ == "__main__":
    main()
