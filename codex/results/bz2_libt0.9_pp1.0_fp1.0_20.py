import bz2
bz2_comp = bz2.BZ2Compressor()
print(bz2_comp.compress(b'hello world!'))
print(bz2_comp.flush())

bz2_decomp = bz2.BZ2Decompressor()
print(bz2_decomp.decompress(bz2_comp.compress(b'hello world!') + bz2_comp.flush()))

from lzma import compress, decompress
print(compress(b'hello world!'))
print(decompress(compress(b'hello world!')))


from urllib.request import urlopen
from io import TextIOWrapper
from urllib.request import urlopen
from urllib.parse import urlencode
from io import StringIO

text_page = urlopen("https://docs.python.org/3.4/library/index.html")
print(TextIOWrapper(text_page).read())

query_args = { 'q': 'query string', 'foo': 'bar' }
encoded_args
