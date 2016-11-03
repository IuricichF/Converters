#!/bin/bash


wget -i getData.txt

FILE='./*.nc'
for f in $FILE
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  python netcdfToPng.py $f 
done
