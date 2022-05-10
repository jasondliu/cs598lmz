import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'reddit_analysis',
    'raise_on_warnings': True,
    'charset': 'utf8mb4',
    'use_unicode': True
}


conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute("TRUNCATE TABLE comments;")
cursor.execute("TRUNCATE TABLE submissions;")

# cursor.execute("ALTER TABLE comments DELETE id;")
# cursor.execute("ALTER TABLE submissions DELETE id;")

conn.commit()
cursor.close()
conn.close()

# conn = mysql.connector.connect(**config)
# cursor = conn.cursor()
# cursor.execute("SELECT COUNT(*) FROM comments;")
# row = cursor.fetchone()
#
