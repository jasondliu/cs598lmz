import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitter_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Create a cursor and execute the sql query
cursor = connection.cursor()
cursor.execute("SELECT * FROM `tweets`")

# Fetch all the rows
data = cursor.fetchall()

# Close the connection
connection.close()

# Show one sample search query
print(data[0])

# Convert to list
data_text = pd.DataFrame(data)
data_text['tweet_text'] = data_text['tweet_text'].astype(str)
data_text = data_text[data_text['tweet_text'] != 'nan']

# Show all the head of the tweet text
