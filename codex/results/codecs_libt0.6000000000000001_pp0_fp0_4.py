import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="",  # password
                     db="sociallogin",
                     charset='utf8mb4',
                     use_unicode=True)

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM users")

# print the first and second columns
for row in cur.fetchall():
    print row[0], " ", row[1]

# Close the cursor
cur.close()

# Close the database connection
db.close()
