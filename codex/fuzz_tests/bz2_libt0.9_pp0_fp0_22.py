import bz2
bz2file_handler = bz2.BZ2File('../data/tweets.json.bz2', 'r')
data = json.loads(bz2file_handler.read().decode('utf-8'))
data.sort(key=lambda item: item['created_at'], reverse=False)
# print data[0:3]

# 9. We will now do some filtering for the data. First, weed out the retweets. Then, let's only consider the tweets with at least one hashtag. Print the number of tweets with hashtags. 
#
# 9.1. Weed out retweets. Retweets should have a field 'retweeted_status' in their JSON representation. 
# Hints: Use 'in' to check if a certain key exists in a dictionary. The 'in' operator checks if a value exists in a container. For strings, 'in' checks if a substring is in the main string. 

# ANSWER:
data_original_tweets = [item for item in data if 'retweeted_status' not in item.keys()]

