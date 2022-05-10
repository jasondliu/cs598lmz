from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

# base64
import base64
base64.b64decode(s)

# hex
import codecs
codecs.decode(s, "hex")

# rot-13
import codecs
codecs.decode(s, "rot-13")

# url
import urllib
urllib.parse.unquote_plus(s)

# utf-8
# s.decode("utf-8")

# utf-16
# s.decode("utf-16")

# gzip
import gzip
gzip.decompress(s)

# zlib
import zlib
zlib.decompress(s)
