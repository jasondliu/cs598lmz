from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('PRAGMA table_info(stocks)')
c.execute('SELECT * FROM stocks')
c.fetchall()

import requests
r = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
r.status_code
len(r.text)
r.text[:75]

import webbrowser
webbrowser.open('http://inventwithpython.com/')

import os
os.path.join('usr', 'bin', 'spam')

os.getcwd()
os.chdir('/server/accesslogs')
os.makedirs('/tmp/delicious/walnut/waffles')

os.path.abspath('.')
os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))

os.path.relpath
