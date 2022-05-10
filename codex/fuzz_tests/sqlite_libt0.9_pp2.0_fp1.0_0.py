import ctypes
import ctypes.util
import threading
import sqlite3
import string
import platform
import os

if sys.platform=='win32':
	bit=re.compile(r'(.*?) (\([a-z]+32\))').findall(platform.architecture()[0])
	if len(bit)!=1 or not bit[0][1]:
		raise 'This seems to be a server operating system. Server OSes not supported!'
	if bit[0][0].lower() != 'win':
		raise 'This seems to be a server operating system. Server OSes not supported!'
	windll = ctypes.windll
		
def check_bitness(key,dictdata):	
	db=sqlite3.connect('Hardware.db')
	db.row_factory = sqlite3.Row
	cursor = db.cursor()
	key.windows_profile = dictdata
	cursor.execute(
			'''SELECT RegistryValue, ValueType FROM RegistryValues WHERE Name = ?;''', 
			(key.registry_key,),
		)
	results = cursor
