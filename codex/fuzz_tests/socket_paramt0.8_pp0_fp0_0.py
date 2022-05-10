import socket
socket.if_indextoname(1)

import requests
r = requests.get('https://github.com/timeline.json')
 
# 'Content-Encoding': 'gzip'

import gzip
f = gzip.GzipFile(fileobj=StringIO.StringIO(r.content))
json.load(f)

# 'Content-Encoding': 'deflate'
zlib.decompress(r.content, -zlib.MAX_WBITS)

# 'Content-Encoding': 'identity'
r.raw.read()

# 'Content-Encoding': 'x-gzip'


import lxml.html
t = lxml.html.fromstring(r.text)
t.cssselect('div.content div.header a')[0]

import re
import json
r = requests.get('https://api.github.com/events')
[(e['type'], e['actor']['login']) for e in r.json()]

r = requests.post('url', data=json.dumps(payload))
r = requests
