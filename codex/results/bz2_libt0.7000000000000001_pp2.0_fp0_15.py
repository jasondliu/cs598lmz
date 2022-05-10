import bz2
bz2.decompress(data).decode('utf-8')

import json
json_data = json.loads(data)
json_data

for entry in json_data['feed']['entry'][0:6]:
    print(entry['title']['$t'])

import feedparser
d = feedparser.parse('http://planet.python.org/rss20.xml')
d['feed']['title']
d['entries']
len(d['entries'])
post = d['entries'][0]
post.keys()
post.title
content = post.content[0].value
print(content[:70])

import nltk
raw = BeautifulSoup(content).get_text()
tokens = nltk.word_tokenize(raw)
tokens

import feedparser
llog = feedparser.parse('http://languagelog.ldc.upenn.edu/nll/?feed=atom')
llog['feed']['title']
len(llog.entries)
post = llog
