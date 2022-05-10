import mmap
import csv
import json
import math
from collections import defaultdict

def find(lst, a):
    return [i for i, x in enumerate(lst) if x == a]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def load_sample_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append({'id': row[0], 'last_name': row[1], 'first_name': row[2], 'department': row[3], 'salary': float(row[4])})
        return data

def load_json_data(filename):
    with open(filename) as data:
        json_data = json.load(data)
        return json_data

def save_json_data(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

