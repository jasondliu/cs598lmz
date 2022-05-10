import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# connect to the MySQL server
conn = pymysql.connect(host='localhost',
                       port=3306,user='root',
                       passwd='password',
                       db='mysql',
                       charset='utf8mb4')

# create a Cursor object
cur = conn.cursor()

# execute a SQL query using execute() method.
cur.execute("USE scraping")

# get the number of rows in the resultset
print(cur.rowcount)

# close the communication with the MySQL
cur.close()
conn.close()

# execute a SQL query using execute() method.
cur.execute("USE scraping")

# store the first result into a variable
data = cur.fetchone()

# print the first result
print(data)

# close the communication with the MySQL
cur.close()
conn.close()

# execute a SQL query using execute() method.
cur.execute("USE scraping")

# store all the
