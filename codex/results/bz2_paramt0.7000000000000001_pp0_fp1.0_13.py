from bz2 import BZ2Decompressor
BZ2Decompressor(dict_size=100000,
                ignore_checksum=True,
                small=False)

# problem 9
import datetime
today = datetime.datetime.today()
today.year
today.month
today.day

# problem 10
import json
json.loads('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
json.dumps([{"a": "A", "c": 3.0, "b": [2, 4]}])

# problem 11
import csv
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
print(mpg[:3])
len(mpg)
mpg[0].keys()
sum(float(d['cty']) for d in mpg) / len(mpg)
sum(float(d['hwy']) for d in mpg) / len(mpg)
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)
CtyMpgBy
