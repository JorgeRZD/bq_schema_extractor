#!/bin/bash

text="GCPProject.Dataset.tableName"
IFS='.'
read -ra array1 <<< "$text"
#echo "$text" | read -ar array1
echo "${array1[2]}"
echo "${array1[1]}"
echo "${array1[0]}"
GCPproject="${array1[0]}"
BQdataset="${array1[1]}"
BQtable="${array1[2]}"
echo "$GCPproject":"$BQdataset"."$BQtable"