import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, sqlite3.Row
import time

'''Setup and create database
    1) First create the database connection instance and setup database name, tables and columns
    2) Use the pointer for different database commands
'''

ts1 = time.time()

# database.cursor(buffered)
# buffered = True|False
#        it tells Python to create a buffer inside the database object, 
#        through which results will be passed.
try:
    database = sqlite3.connect('customer.db', timeout=10)
    database_curs = database.cursor()

except Error as e:
    print(e)
    print('Error: Unable to conntect sqlite3 database')
    database = None

try:
    database_curs.execute(""" CREATE TABLE customers(
                                customer_id int, 
                                first_name text,
                                last_name text,
                                street text,
                                city text,
                                state char(2),
                                zipcode char(5),
                                pnumber1 char(3),

