import mmap
import csv
import os
import sys
from collections import defaultdict
from collections import Counter


def main():
    #if len(sys.argv) != 2:
    #    sys.exit('Usage: {0} <csv_file>'.format(sys.argv[0]))

    #mm = mmap.mmap(csv_file.fileno(), 0, access=mmap.ACCESS_READ)
    #csv_file = open(sys.argv[1], "r+")

    #csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    #headers = next(csv_reader)
    #column = {}
    #for h in headers:
    #    column[h] = []

    #for row in csv_reader:
    #    for h, v in zip(headers, row):
    #        column[h].append(v)

    #column_count = Counter()
    #for _, values in column.items():
    #    column_count.update(values)

    #print
