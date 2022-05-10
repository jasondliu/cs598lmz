import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite_file = 'test.sqlite'    # name of the sqlite database file
table_name = 'my_table_3'   # name of the table to be created
id_column = 'my_1st_column' # name of the PRIMARY KEY column
new_field = 'my_2nd_column'  # name of the new column
field_type = 'INTEGER'  # column data type

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('CREATE TABLE {tn} ({fn} {ft} PRIMARY KEY)'\
        .format(tn=table_name, fn=id_column, ft=field_type))
conn.commit()
conn.close()
# connect to database and 
conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()
