from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/home/michael/Downloads/enwiki-latest-pages-articles.xml.bz2', 'rb').read())

from bz2 import BZ2Decompressor
from io import BytesIO

with open('/home/michael/Downloads/enwiki-latest-pages-articles.xml.bz2', 'rb') as compressed_file:
    decompressor = BZ2Decompressor()

    data = decompressor.decompress(compressed_file.read())

    for line in BytesIO(data):
        print(line)

from bz2 import BZ2Decompressor
from io import BytesIO

with open('/home/michael/Downloads/enwiki-latest-pages-articles.xml.bz2', 'rb') as compressed_file:
    decompressor = BZ2Decompressor()

    data = decompressor.decompress(compressed_file.read())

    for line in BytesIO(data):
        print(line.decode('utf-8'))

from b
