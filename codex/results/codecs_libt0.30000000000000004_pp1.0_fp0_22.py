import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# mysql.connector
import mysql.connector
from mysql.connector import errorcode

# Connect to the database
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')

cursor = cnx.cursor()

# Create a new record
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)

cnx.commit()

print(cursor.rowcount, "record inserted.")

# Close the connection
cnx.close()
