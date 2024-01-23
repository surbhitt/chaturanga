#!/usr/bin/env python3
import os

with open ('pieceurl.txt' , 'r') as f:
    for line in f.readlines():
        os.system(f"wget {line}")
