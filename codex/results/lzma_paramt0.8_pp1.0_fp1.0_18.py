from lzma import LZMADecompressor
LZMADecompressor()

from bz2 import decompress
decompress(bz2_data)

from gzip import decompress
decompress(gzip_data)

from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

"""

"""
# 11.4. xml.etree.ElementTree — The ElementTree XML API
# https: // docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as etree
tree = etree.parse('country_data.xml')
print(type(tree))
print(tree)
print(t)
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
print(t)
for child in root:
    print(child.tag, child.attrib)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for neighbor in root.iter('neighbor'):

