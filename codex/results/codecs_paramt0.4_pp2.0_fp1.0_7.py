import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Indexer(object):
    """
    Indexer for the IMDB dataset.
    """

    def __init__(self, index_path):
        """
        Initializes the indexer.

        Args:
            index_path: Path to where the index will be stored.
        """
        self.index_path = index_path
        self.index = None

    def create_index(self, data_path, limit=None):
        """
        Creates the index from the dataset.

        Args:
            data_path: Path to the dataset.
            limit: The maximum number of documents to index.
        """
        self.index = index.create_in(self.index_path, schema.Schema())

        writer = self.index.writer()

        with codecs.open(data_path, 'r', 'utf-8', 'strict') as f:
            for i, line in enumerate(f):
                if limit and i >= limit:
                    break

                data = json.loads(line.strip
