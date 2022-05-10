import codecs
codecs.register_error('strict', codecs.ignore_errors)

class EbookList(object):

    def __init__(self, name, filename, category=None):
        self.name = name
        self.filename = filename
        self.category = category
        self.books = []

    def parse(self, dirname):

        tree = ET.parse(os.path.join(dirname, self.filename))
        root = tree.getroot()

        for book in root.findall('book'):
            title = book.find('title').text
            author = book.find('author').text
            filename = book.find('filename').text
            self.books.append(Ebook(dirname, title, author, filename))
        print('Found %d books in %s.' % (len(self.books), self.name))

    def write(self, outfile):
        outfile.write('<category>\n')
        outfile.write('<name>%s</name>\n' % self.name)
        for book in self.books:
            book.write(
