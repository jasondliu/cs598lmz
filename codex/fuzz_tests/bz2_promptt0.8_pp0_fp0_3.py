import bz2
# Test BZ2Decompressor
data = open('../sources/wiki/enwiki-latest-pages-articles.xml.bz2', 'rb').read()
bz_decomp = bz2.BZ2Decompressor()
data = bz_decomp.decompress(data[:10])
def wiki_parser(file):
    for event, elem in etree.iterparse(file, events=('end',)):
        if event == 'end':
            if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}page':
                yield elem
                elem.clear()

def get_text(elem):
    return elem.find('.//{http://www.mediawiki.org/xml/export-0.10/}text').text

def get_title(elem):
    return elem.find('{http://www.mediawiki.org/xml/export-0.10/}title').text

def get_id(elem):
    return elem.find('{http://www.mediawiki.
