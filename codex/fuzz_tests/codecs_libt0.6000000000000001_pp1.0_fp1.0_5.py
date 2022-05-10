import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up a connection to the database
conn = MySQLdb.connect(host='127.0.0.1',
                       user='root',
                       passwd='',
                       db='Tweet_Scraper',
                       use_unicode=True,
                       charset='utf8mb4')
c = conn.cursor()

# Create a table to store the tweets
c.execute('''CREATE TABLE IF NOT EXISTS tweet_scraper
             (ID INT PRIMARY KEY AUTO_INCREMENT,
              user_id VARCHAR(50),
              user_name VARCHAR(255),
              tweet_id VARCHAR(255),
              tweet_text TEXT,
              tweet_date DATETIME,
              tweet_source VARCHAR(255),
              tweet_retweets INT,
              tweet_favorites INT,
              tweet_replies INT,
              tweet_mentions TEXT,
              tweet_hashtags TEXT,
              tweet_
