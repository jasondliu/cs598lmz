import codecs
codecs.register_error('strict', codecs.ignore_errors)

class UnicodeCSV:
    def __init__(self,f, encoding="utf-8", **kwargs):
        self.encoding = encoding
        self.csv_reader = csv.reader(f, **kwargs)
    def next(self):
        '''next() -> unicode
        This function reads and returns the next line as a Unicode strin
