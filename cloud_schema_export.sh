#!/bin/bash
GCPproject="$1"
BQdataset="$2"
BQtable="$3"

echo "Target table: ${GCPproject}:${BQdataset}.${BQtable}"

bq show --schema --format=prettyjson "${GCPproject}:${BQdataset}.${BQtable}">${BQdataset}-${BQtable}.json

echo "+++ Schema exported to {$PWD} +++"