import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# https://stackoverflow.com/questions/34293875/how-to-remove-spaces-in-pandas-dataframe
df.columns = df.columns.str.replace(' ', '')

# https://stackoverflow.com/questions/28384588/twitter-api-get-tweets-with-specific-id
import tweepy
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

tweet = api.get_status(tweet_id, tweet_mode='extended')
print(f"{tweet.full_text}")

# https://stackoverflow.com/questions/16511337/correctly-saving-json-data-from-twitter-api-with-python
import json

with open('tweet.json', 'w')
