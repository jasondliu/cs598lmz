from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/home/nate/Downloads/enwiki-20150304-pages-articles-multistream.xml.bz2', 'rb').read())

#this is what we are using
with bz2.BZ2File('/home/nate/Downloads/enwiki-20150304-pages-articles-multistream.xml.bz2', 'r') as f:
    content = f.read()
    print(content)

#this is what we are using
with bz2.BZ2File('/home/nate/Downloads/enwiki-20150304-pages-articles-multistream.xml.bz2', 'r') as f:
    content = f.read()
    print(content)

#this is what we are using
with bz2.BZ2File('/home/nate/Downloads/enwiki-20150304-pages-articles-multistream.xml.bz2', 'r') as f:
    content = f.read()
    print(content)

#this
