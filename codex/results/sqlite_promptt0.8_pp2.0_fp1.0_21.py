import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('myfile.db')
# This will create a new database if a file called myfile.db doesn't already exist.
# conn = sqlite3.connect('myfile.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE stock_cash_flow
#              (date text, trans text, symbol text, qty real, price real)''')
# conn.commit()
# conn.close()
# cursor.execute('''CREATE TABLE {}
#               (id integer primary key autoincrement,name varchar(20),address text)'''
#               .format('users'))
# cursor.commit()

# Load the library
lib_path = '../lib/libCTP_Quote.so'
ctp_lib = ctypes.cdll.LoadLibrary(lib_path)

# Declare the signature of the function we are going to call from the library
ctp_lib.CTP_Subscribe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]

