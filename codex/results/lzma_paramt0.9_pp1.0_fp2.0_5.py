from lzma import LZMADecompressor
LZMADecompressor(stream=12)


import dill
dill.load(12)
dill.dumps(12, protocol=None)


import pickletools
pickletools.dis(12)
pickletools.optimize(12)
pickletools.genops(12)


import cPickle
cPickle.HIGHEST_PROTOCOL
cPickle.HIGHEST_PROTOCOL = 1
cPickle.HIGHEST_PROTOCOL
cPickle.dumps(12, 1, protocol=2)


import csv
csv.register_dialect("dialect", delimiter="delim", quoting="all")


import sqlite3
sqlite3.complete_statement("sql")
sqlite3.connect("":memory:")
sqlite3.connect("file.db", 3, "My objects table", detect_types=None, isolation_level=None, check_same_thread=None, factory=None, cached_statements=100)
sqlite3.connect("file.db", uri=True, detect_types=None, isolation_
