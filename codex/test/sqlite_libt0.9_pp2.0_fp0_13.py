import ctypes
import ctypes.util
import threading
import sqlite3

import dropbox

def main():
	dbx = dropbox.Dropbox("INSERT_TOKEN_HERE")
	account_info = dbx.users_get_current_account().name
	print("Using account " + account_info.given_name + " " +  account_info.surname)
	print("")
	print("")

	dbx.users_get_space_usage()

	dbx.users_get_current_account()

	conn = sqlite3.connect("/home/pi/python_programs/iot/config.db")
	cursor = conn.cursor()
	cursor.execute('SELECT name FROM sqlite_master WHERE type = "table" AND name = "users"')

	result = cursor.fetchone()

	if(len(result) == 0):
		print("No users table exists. Will create.")
