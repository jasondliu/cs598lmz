import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO: add support for other formats
# TODO: add support for other languages

class Corpus(object):
    """
    A corpus is a collection of documents.
    """

    def __init__(self, documents=None, name=None):
        """
        Initialize a corpus.

        :param documents: a list of documents
        :type documents: list of :class:`Document`
        :param name: the name of the corpus
        :type name: str
        """
        self.name = name
        self.documents = documents or []

    def __iter__(self):
        """
        Iterate over the documents in the corpus.

        :return: an iterator over the documents
        :rtype: iterator of :class:`Document`
        """
        return iter(self.documents)

    def __len__(self):
        """
        Return the number of documents in the corpus.

        :return: the number of documents in the corpus
        :rtype: int
        """
        return len(self.
