from bz2 import BZ2Decompressor
BZ2Decompressor

from lxml import etree

class DumpFile:

    def __init__(self, path):
        self.path = path

    def __iter__(self):

        decompressor = BZ2Decompressor()

        for event, el in etree.iterparse(self.path, events=['end']):
            if el.tag[el.tag.find('}')+1:] == 'page':
                yield {
                    'id': el.findtext('./id'),
                    'title': el.findtext('./title'),
                    'ns': el.findtext('./ns'),
                    'revision': el.find('./revision'),
                }
                el.clear()


if __name__ == '__main__':
    for page in DumpFile('wikipedia_pages_current.xml.bz2'):
        print(page['id'], page['title'])
</code>

Using the <code>lxml</code> <code>iterparse</code> function, you can read the data without having to load the whole file into
