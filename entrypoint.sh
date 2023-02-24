#!/bin/sh

python /app/main.py
[ $? -eq 0 ]  || exit 1
