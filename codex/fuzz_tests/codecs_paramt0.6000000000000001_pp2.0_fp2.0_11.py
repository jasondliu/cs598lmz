import codecs
codecs.register_error('ignore_invalid', codecs.ignore_errors)

class Book(object):
    def __init__(self, book_path, output_path):
        self.book_path = book_path
        self.output_path = output_path
        self.book_name = os.path.basename(self.book_path)
        self.book_name = self.book_name[:self.book_name.find('.')]
        self.output_file = os.path.join(self.output_path, self.book_name)

    def __get_chapters(self):
        """
        Returns a list of the chapters in the book.
        """
        chapters = []
        with open(self.book_path) as book_file:
            for line in book_file:
                line = line.strip()
                if line.startswith('Chapter'):
                    chapters.append(line)
        return chapters

    def __title_to_filename(self, title):
        """
        Convert a chapter title to a valid filename.
        """
        title
