import codecs
codecs.register_error('replace_spaces', lambda e: (u' ',e.start + 1))

class TaggedCorpusReader(CorpusReader):
    """
    A corpus reader for raw text documents with part-of-speech tags.
    """
    TOKEN_SEP = ' '
    TAG_SEP = '/'
    
    def __init__(self, root, fileids, word_tokenizer=WordPunctTokenizer(),
                 pos_tokenizer=WhitespaceTokenizer(),
                 tagset=None, encoding='utf8'):
        """
        Construct a new Tagged Corpus reader for a set of documents
        located at the given root directory.  Example usage:
        
            >>> from nltk.corpus import BracketParseCorpusReader
            >>> from nltk.tokenize import RegexpTokenizer
            >>> root = r'C:\Corpus\BNC'
            >>> reader = BracketParseCorpusReader(root, r'[A-K]/wsj_.*\.mrg')
            >>> pos_reader = TaggedCorpusReader(root, r
