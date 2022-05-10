import mmap
import sys
import os

def database_setup(path):
	path = os.path.abspath(path)
	db = sqlite3.connect(path)
	c = db.cursor()
	#c.execute('create table if not exists storage (hash text primary key, last_used integer, round_used text, offset text, size text, path text);')
	#c.execute('create table if not exists hash_storage (hash text primary key, offset text, size text);')
	c.execute('create table hash_storage (hash text primary key, offset text, size text, path text);')
	db.commit()
	return c
	
def database_close(c):
	c.close()
	
def hash_chunk(chunk):
	m = hashlib.sha256()
	m.update(chunk)
	return m.digest()
	
def add_chunk(c, chunk, offset, size, path):
	c.execute('select * from hash_storage where hash=?', (hash_chunk(chunk),))
