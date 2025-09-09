# BigQuery schema extractor
This script is aimed to easily and safely retrieve table information from BigQuery.

The shell script `cloud_schema_export.sh` should be ran in Cloud Shell as a mean to extract the schema to the root working directory in standarized json format so it can be downloaded to a local instance. 

The python script `schema_extractor.py` uses the json output of `cloud_schema_export.sh` and is intended to print all the column names of the table in a list format separated by line breaks to use in spreadsheet apps. Additionally, declaring that data type is required causes the script to include the data type, as it is declared in Bigquery, so that it can be inserted directly in DDL statements.
