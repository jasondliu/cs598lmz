import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  
#-------------------------------------------------------------------------------
class CsvFile(object):
    """
    """
    def __init__(self, filename, delimiter = ';', quotechar = '"', 
                 encoding = 'utf-8', **kwargs):
        """
        """
        self.filename = filename
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.encoding = encoding
        
        self.kwargs = kwargs

    def __iter__(self):
        """
        """
        with codecs.open(self.filename, 'r', self.encoding, 'strict') as f:
            reader = csv.reader(f, delimiter = self.delimiter, 
                                quotechar = self.quotechar, **self.kwargs)
            for row in reader:
                yield row

    def __len__(self):
        """
        """
        with codecs.open(self.filename, 'r', self.encoding, 'strict')
