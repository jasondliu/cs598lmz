import lzma
lzma.LZMAError

import os
os.getcwd()
os.chdir('/Users/jason/Documents/GitHub/Python/Python_Crash_Course/Chapter_10/')
os.getcwd()

import json
json.dumps([1, 'simple', 'list'])

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

json.dumps(d)

import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

json.loads('"\\"foo\\bar"')

json.loads('"\\"foo\\bar"')

json.loads('"\\"foo\\bar"')

json.loads('"\\"foo\\bar"')

json.loads('"\\"foo\\bar"')

json.loads('"\\"
