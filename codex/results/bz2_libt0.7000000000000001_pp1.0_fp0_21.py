import bz2
bz2_file = bz2.BZ2File('/home/jovyan/work/data/test.json.bz2')
for line in bz2_file:
    print(line)

import json
for line in bz2_file:
    record = json.loads(line)
    print(record)

# Function to generate a sample for each file
def generate_sample(file, k=10):
    with open(file, 'rb') as open_file:
        for i, line in enumerate(open_file):
            if i <= k:
                record = json.loads(line)
                print(record)
            else:
                break

generate_sample('/home/jovyan/work/data/test.json.bz2')

# List comprehension to generate a list of files that match a pattern
import os
import glob
file_list = [f for f in glob.glob('/home/jovyan/work/data/*.json.bz2')]
file_list

for file in file_list:
   
