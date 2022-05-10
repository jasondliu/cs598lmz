import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Define the path to the data
path = './data/'

# Define the list of files to process
files = ['tweets_#gohawks.txt', 'tweets_#gopatriots.txt', 'tweets_#nfl.txt',
         'tweets_#patriots.txt', 'tweets_#sb49.txt', 'tweets_#superbowl.txt']

# Define the list of features
features = ['number of tweets', 'number of retweets', 'number of followers',
            'max number of followers', 'time of day', 'day of week']

# Define the list of labels
labels = ['tweets_#gohawks.txt', 'tweets_#gopatriots.txt', 'tweets_#nfl.txt',
          'tweets_#patriots.txt', 'tweets_#sb49.txt', 'tweets_#superbowl.txt']
# Define a function
