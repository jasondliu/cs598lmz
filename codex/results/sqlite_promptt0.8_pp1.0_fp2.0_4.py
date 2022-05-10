import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() method
# if the database is not there, it creates a new database
conn = sqlite3.connect('stock.db')
print 'opened database successfully'

# create a table
conn.execute('''
	create table stock (
	id integer primary key,
	name text,
	price text)
	''')

# Addin a record
conn.execute('insert into stock (name, price) values (?,?)', ('Intel', '128.08'))
conn.commit()

# Add another record
conn.execute('insert into stock (name, price) values (?,?)', ('AMD', '15.56'))
conn.commit()

# Retrieve data
cursor = conn.execute('select * from stock where id = ?', ('1',))
for row in cursor:
	print 'id = ', row[0]
	print 'name = ', row[1]
	print 'price = ', row[2]

print 'operation done successfully'

# Close connection
conn.close()

# Test sqlite3.connect() method
conn = sqlite3.connect('
