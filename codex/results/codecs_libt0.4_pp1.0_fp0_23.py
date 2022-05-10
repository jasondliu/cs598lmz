import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='fakenews',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Create a new cursor
cur = conn.cursor()

# Select all of the historic Google Trends data
cur.execute("SELECT * FROM google_trends")

# Load it into a pandas dataframe
trends_df = pd.DataFrame(list(cur.fetchall()))

# Select all of the historic Reddit submissions
cur.execute("SELECT * FROM reddit_submissions")

# Load it into a pandas dataframe
submissions_df = pd.DataFrame(list(cur.fetchall()))

# Select all of the historic Reddit comments
cur.execute("SELECT * FROM reddit_comments")

# Load it into
