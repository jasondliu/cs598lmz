import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='twitter')
cursor = cnx.cursor()

# Twitter API
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

# Get all users from the DB
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
	print "Getting tweets for user: " + user[1]

	# Get tweets for the user
	try:
		tweets = twitter.get_user_timeline(screen_name=user[1], count=200)
	except TwythonError as e:
		print e
		continue

	for tweet in tweets:
		# Check if tweet already exists
		cursor.execute("SELECT * FROM tweets WHERE id = %s", (tweet['id'],))
		if
