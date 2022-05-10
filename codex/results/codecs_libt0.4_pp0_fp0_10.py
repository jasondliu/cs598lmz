import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# connect to the MySQL server
conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="yelp_db",
                       charset='utf8mb4')

# create a cursor
cursor = conn.cursor()

# execute an SQL statement
cursor.execute("SELECT * FROM yelp_db.business;")

# retrieve the rows
rows = cursor.fetchall()

# print the rows
for row in rows:
    print(row)

# close the cursor
cursor.close()

# close the connection
conn.close()

# print the rows
for row in rows:
    print(row)
 
# close the cursor
cursor.close()

# close the connection
conn.close()

# create a cursor
cursor = conn.cursor()

# execute an SQL statement
cursor.execute("SELECT * FROM yelp_db.business
