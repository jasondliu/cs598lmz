from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz_bytes)

import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(x)")
conn.execute("INSERT INTO t VALUES ('abc')")

import logging
logging.basicConfig(filename='app.log')
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so')

from datetime import date
now = date.today()
after = now.replace(year=now.year+1)
now
after

import hashlib
hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()

import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.crc32(s)

from io import StringIO, BytesIO
output = BytesIO()
output.write(b'this goes into the buffer. ')
output.write(b'and so does this
