from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(wiki_data)
with open('/tmp/wiki.xml', 'wb') as f:
    f.write(BZ2Decompressor().decompress(wiki_data))
    
from lxml import etree
tree = etree.parse("/tmp/wiki.xml")

from nltk.tokenize import sent_tokenize, word_tokenize
for link in tree.iter("link"):
    source = link.get("title")
    target = link.get("dest")
    print (source,"==>", target)
