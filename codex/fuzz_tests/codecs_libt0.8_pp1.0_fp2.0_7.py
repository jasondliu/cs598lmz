import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

with open('/Users/jguillaumes/Documents/GitHub/data/tweets_morrissey_04_22.json', 'r') as f:
    tweets = json.load(f)
    tweets = tweets['tweets']
f.close()

#tweetstext = []
#for tweet in tweets:
#    if len(tweet['annotations']) == 0:
#        tweetstext.append(tweet['text'])

#tweets = tweetstext
tweets = [tweet['text'] for tweet in tweets if len(tweet['annotations']) == 0]

print tweets[2]

text = ""
text += '\n'.join(tweets)

# f.write(text.encode('utf8'))

with open('/Users/jguillaumes/Documents/GitHub/data/tweets_morrissey_04_22.txt', '
