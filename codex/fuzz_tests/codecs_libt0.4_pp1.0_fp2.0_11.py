import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#-------------------------------------------------------------------------------
# Connect to MySQL
#-------------------------------------------------------------------------------

# Connect to the MySQL instance
db_conn = pymysql.connect(host="localhost",
                     user="root",
                     db="twitter",
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

#-------------------------------------------------------------------------------
# Query Twitter Data
#-------------------------------------------------------------------------------

# Query the database and obtain data as Python objects
db_cursor = db_conn.cursor()
db_cursor.execute("""
SELECT *
FROM twitter
""")

# Store Twitter data in a DataFrame: twitter_df
twitter_df = pd.DataFrame(db_cursor.fetchall())

# Close connection to MySQL
db_conn.close()

#-------------------------------------------------------------------------------
# Define TextBlob Sentiment Analyzer
#-------------------------------------------------------------------------------

def detect_sentiment(text):
    return TextBlob(text.decode('utf
