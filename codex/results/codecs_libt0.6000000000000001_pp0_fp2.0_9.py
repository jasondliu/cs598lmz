import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitter_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Create a new cursor
cur = connection.cursor()

#print(cur.execute("SELECT * FROM twitter_data.twitter_table"))

# Print all results
#print(cur.fetchall())

# Print the first result
#print(cur.fetchone())

#print(cur.execute("SELECT * FROM twitter_data.twitter_table WHERE tweet LIKE '%#%' "))

# Print all results
#print(cur.fetchall())

#print(cur.execute("SELECT * FROM twitter_data.twitter_table "))

# Print all results
#print(cur.fetchall())

#print
