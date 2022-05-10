import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO:
# - add support for other file types (e.g. .docx)
# - add support for other languages (e.g. German)
# - add support for other corpora (e.g. Brown)
# - add support for other tokenizers (e.g. NLTK)
# - add support for other taggers (e.g. NLTK)
# - add support for other parsers (e.g. NLTK)
# - add support for other chunkers (e.g. NLTK)

class Corpus(object):
    """
    A corpus is a collection of documents.
    """
    def __init__(self, name, path, file_type='txt', encoding='utf-8',
                 tokenizer=None, tagger=None, parser=None, chunker=None):
        """
        Initialize a corpus.

        @param name: The name of the corpus.
        @type name: C{str}
        @param path: The path to the corpus.
        @type path
