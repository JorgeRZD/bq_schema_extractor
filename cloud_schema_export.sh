#!/bin/bash
GCPproject="$1"
BQdataset="$2"
BQtable="$3"
target="$GCPproject:$BQdataset.$BQtable"

echo "++++ Target table: $target ++++"
sleep 3
echo "++++ Checking if table exists ++++"

bq show --schema $target>/dev/null

if [[ $? -ne 0]]; then 
    echo "++++ table $target does not exist. Make sure parameters are correct ++++"
else
    echo "++++ Table exists. Proceeding to export schema ++++"
    bq show --schema --format=prettyjson "$target">${BQdataset}-${BQtable}.json
    echo "+++ Schema exported to {$PWD}/${BQdataset}-${BQtable}.json +++"
fi