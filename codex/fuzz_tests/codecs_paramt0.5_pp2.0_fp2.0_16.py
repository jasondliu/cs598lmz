import codecs
codecs.register_error('strict', codecs.ignore_errors)

class LazyCorpusLoader(object):
    def __init__(self, name, reader_cls, *args, **kwargs):
        self.name = name
        self.reader_cls = reader_cls
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return CategorizedCorpusReader(self.name, self.reader_cls, *self.args, **self.kwargs)

class CategorizedCorpusReader(object):
    """
    A corpus reader for categorized text documents to allow efficient
    access to documents in a particular category.
    """
    def __init__(self, root, reader_cls, *args, **kwargs):
        """
        Construct a new categorized corpus reader for a set of documents
        located at the given root directory.  Categorization of the
        documents is done based on subdirectory names, with each
        subdirectory representing a category.  The reader_cls is the
        corpus
