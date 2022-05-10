import bz2
bz2.open('file.bz2')

# xml
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

# csv
import csv
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# sql
import sqlite3
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Counts ORDER BY count DESC LIMIT 10')
for row in cur:
    print(row)
