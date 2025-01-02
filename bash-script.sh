#! /bin/bash 

if test "$#" -ne 3; then 
echo "Syntax error. Missing arguments"
echo "Usage: ./bash-script.sh #cpubenchs #iobenchs case_name"
else
python3 python-script.py $1 $2 > raw_mediciones_RR/$3.out
fi