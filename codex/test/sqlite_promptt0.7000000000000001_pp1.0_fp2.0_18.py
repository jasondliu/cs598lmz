import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() function
# For more information:
# https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3%20connect
# https://www.tutorialspoint.com/python/python_database_access.htm
# https://www.tutorialspoint.com/python/python_database_access.htm

# Create a connection object
connection = sqlite3.connect("test.db")

# Create a cursor object
cursor = connection.cursor()

# Create a table
sql_command = """
CREATE TABLE IF NOT EXISTS employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""

# Execute the statement
cursor.execute(sql_command)

# Close the connection
connection.close()
# Test sqlite3.connect() function
# For more information:
# https://docs.python.org/3/library/sqlite3.html?highlight=sql
