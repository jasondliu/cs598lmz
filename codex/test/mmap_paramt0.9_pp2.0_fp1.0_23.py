import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(pack('L', 1))
    m.seek(0)
    repr(m)
    m[0]

import sqlite3
import datetime

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('create table first (one varint)')
w = cur.execute('pragma mmap_size').fetchone()[0]
conn.close()

conn = sqlite3.connect(':memory:', isolation_level=None)
cur = conn.cursor()
cur.execute('create table first (one varint)')
w = cur.execute('pragma mmap_size').fetchone()[0]
conn.close()

conn = sqlite3.connect(':memory:', isolation_level=2)
