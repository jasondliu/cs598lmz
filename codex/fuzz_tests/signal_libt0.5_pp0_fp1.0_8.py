import signal
signal.signal(signal.SIGINT, signal_handler)

# Get the last 100 tweets from each of my friends
for friend in tweepy.Cursor(api.friends).items():

    # Process the friend's tweets
    process_or_store(friend._json)

    # Get the last 200 tweets from each of my followers
    for follower in tweepy.Cursor(api.followers).items():

        # Process the follower's tweets
        process_or_store(follower._json)

# Get the last 200 tweets from your own timeline
for status in tweepy.Cursor(api.home_timeline).items(200):
    # Process a single status
    process_or_store(status._json)

# Get the last 200 tweets from your own timeline
for status in tweepy.Cursor(api.home_timeline).items(200):
    # Process a single status
    process_or_store(status._json)

# Get the last 200 tweets from your own timeline
for status in tweepy.Cursor(api.home_timeline).items
