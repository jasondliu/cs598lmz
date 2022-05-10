import ctypes
import ctypes.util
import threading
import sqlite3
import requests
import datetime
import os
import time
import pytz
import json
import sqlite3
import re

def main():
	db_name = "data.db"
	db = sqlite3.connect(db_name)
	c = db.cursor()
	#c.execute('drop table if exists test')
	#c.execute('create table test (id integer primary key, data text)')
	#c.execute('insert into test (data) values ("test")')
	#db.commit()
	#c.execute('select * from test')
	#print(c.fetchall())
	#db.close()
	#return
	
	db_name = "data.db"
	db = sqlite3.connect(db_name)
	c = db.cursor()
	c.execute('drop table if exists usd')
	c.execute('drop table if exists eur')
	c.execute('drop table if exists gbp')
	c.execute('drop table if exists all')
