import bz2
bz2.open('./collections/jawiki-latest-pages-articles1.xml.bz2', 'rt', encoding='utf8') as file :
    line = file.readline()
    while line : 
        print(line.rstrip())
        line = file.readline()

# CSV ファイルの読み込み
import csv
with open('example.csv','r', encoding='utf8') as f : 
    reader = csv.reader(f)
    for row in reader : 
        print(row)

# JSON ファイルの読み込み
import json
f = open('example.json', 'r', encoding='utf8')
json.load(f)

# データベースへの接続
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('CREATE TABLE person (id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')
