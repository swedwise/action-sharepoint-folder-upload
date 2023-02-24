#!/bin/sh -l

python /app/main.py
[ $? -eq 0 ]  || exit 1
