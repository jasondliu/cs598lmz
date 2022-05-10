import bz2
bz2_file = bz2.BZ2File('dickens.txt.bz2')
print bz2_file.readline()
#print bz2_file.readlines()

import csv
reader = csv.reader(open('sp500.csv'))
for row in reader:
            print row

import csv
reader = csv.reader(open('sp500.csv'))
for row in reader:
            print row[0]

import csv
reader = csv.reader(open('sp500.csv'))
for row in reader:
            print row[2]

import csv
reader = csv.DictReader(open('sp500.csv'))
for row in reader:
            print row

import csv
reader = csv.DictReader(open('sp500.csv'))
for row in reader:
            print row['Price']

import csv
reader = csv.DictReader(open('sp500.csv'))
for row in reader:
            print row['Symbol']
