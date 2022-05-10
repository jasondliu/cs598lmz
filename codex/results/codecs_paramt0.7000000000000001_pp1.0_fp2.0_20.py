import codecs
codecs.register_error("strict", codecs.ignore_errors)

# TODO: Use defaultdict(set) as a "bag" instead of a dictionary
# TODO: Look into alternative pinyin representations
# TODO: Add support for Jyutping
# TODO: Add support for Cantonese
# TODO: Make each word's definition a list rather than a string
# TODO: Add support for alternative word forms
# TODO: Figure out how to handle words with multiple definitions in the database

class CantoneseDictionary(object):
    """
    This is a Cantonese dictionary parser for the Cantonese database at:
    http://www.cantonese.sheik.co.uk/dictionary/characters/

    The database is in the form:

    - Word
    - Definition
    - Pronunciation (Jyutping)
    - Traditional Chinese
    - Simplified Chinese
    - Pinyin (Yale)
    - Definition (English)

    This is a simple parser to get the data into a dictionary.
    """

    def __init__(self):
        self.database
