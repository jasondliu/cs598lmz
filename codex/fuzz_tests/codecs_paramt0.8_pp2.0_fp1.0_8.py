import codecs
codecs.register_error('ignore', lambda error: (u'\uFFFD', error.end))

# We do this to ignore some lines that could be problematic for decoding
def ignore_error(data):
    return (u'\uFFFD', data.end)


codecs.register_error('ignore', ignore_error)

class Collection:
    """
    The Collection object manages the storage, metadata, and search
    capabilities of a corpus of text documents.
    """

    def __init__(self):
        """
        Initializes the collection object.
        """
        self.documents = {}        # The set of documents
        self.index = None          # The index generated from the documents
        self.metadata = {}         # Corpus-wide metadata
        self.name = None           # The name of this collection
        self.term_id_map = {}      # Mappings of term strings to indexes
        self.id_term_map = {}      # Mappings of indexes to term strings
        self.metadata = {}         # Metadata for the entire collection
        self.total_token_count = 0 # Total number of
