import csv
import json
from pathlib import Path
import os

chars_pics = set()
for file_name in os.listdir('px_lc'):
    chars_pics.add(file_name[:-4])
missing = set()
with open('data.csv', newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line in reader:
            for p in [1,2,3,4]:
                if line[f'p{p}_lc'] not in chars_pics:
                    missing.add(line[f'p{p}_lc'])
print(missing)


chars_pics = set()
for file_name in os.listdir('px_char'):
    chars_pics.add(file_name[:-4])
missing = set()
with open('data.csv', newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line in reader:
            for p in [1,2,3,4]:
                if line[f'p{p}_char'] not in chars_pics:
                    missing.add(line[f'p{p}_char'])
            
print(missing)
        