import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Use the database file SQLite_Python.db; if it does not exist, this creates a new database
conn = sqlite3.connect('SQLite_Python.db')

# Once a connection has been established, we use the cursor
# object to execute queries
c = conn.cursor()

# Create the table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# Insert a row of data
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t
