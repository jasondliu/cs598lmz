from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(filename, 'rb').read())

filename = 'data/c.json'
from zlib import decompress
decompress(open(filename, 'rb').read())

from json import loads
json_text = decompress(open(filename, 'rb').read())
tweets = loads(json_text)
print('Loaded {} tweets'.format(len(tweets)))

from os import listdir
from os.path import isfile, join

tweet_files = [f for f in listdir(path) if isfile(join(path, f))]

tweet_files

filename = 'data/aj.json.bz2'
f = bz2.BZ2File(filename, 'rb')

f.read(500)

from os import getcwd
getcwd()

from json import loads
tweets = []

for line in f:
    tweet = loads(line.decode('utf-8'))
    tweets.append(tweet)

tweets[0]

f.
