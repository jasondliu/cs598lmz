import codecs
codecs.register_error('strict', codecs.ignore_errors)


def get_tokenizer(lang):
    """Get tokenizer for given language.

    :param lang: language code
    :return: `Tokenizer` instance or None if language not found
    """
    if lang in TOKENIZERS:
        return TOKENIZERS[lang]()


class Tokenizer(object):
    """Tokenizer tokenizes sentences."""

    language = None

    def __init__(self):
        self.tokenizer = None

    def setup_model(self):
        raise NotImplementedError

    def tokenize(self, text):
        """Tokenize given text.

        :param text: input text
        :return: list of tokens
        """
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        """Load tokenizer from given path.
        :param path: path to tokenizer model
        :return: `Tokenizer` instance
        """
        raise NotImplementedError


class NLTKTreebankWordTokenizer(Tokenizer):
    """
