# BigQuery schema extractor
This script is aimed to easily and safely retrieve table information from BigQuery.

The shell script `cloud_schema_export.sh` should be ran in Cloud Shell as a mean to extract the schema to the root working directory in standarized json format so it can be downloaded to a local instance. The shell script validates that the specified direction of GCP project, dataset and table exists and, only if it does, generates a schema json file.

The python script `schema_extractor.py` uses the json output of `cloud_schema_export.sh` and is intended to print all the column names of the table in a list format separated by line breaks to use in spreadsheet apps. Additionally, declaring that data type is required causes the script to include the data type, as it is declared in Bigquery, so that it can be inserted directly in DDL statements.

The view_creator.py is intended to create a folder with the necessary files to create a view from an existing table following the required imputs in Terraform, i.e. a json file containing the view schema and a sql `SELECT... FROM` query. It takes as inputs the name of the json file extracted with `cloud_schema_export.sh` and the name of the column or columns (separated by comma) that will be used as primary key(s).