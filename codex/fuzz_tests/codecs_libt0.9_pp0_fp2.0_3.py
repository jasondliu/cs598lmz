import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# Load tokenizer
TOKENIZER = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)

EMBEDDING_DIM = 300
FASTTEXT_DIR = 'fasttext'

NUMBER_OF_FILES_IN_PRETRAINED_EMBEDDINGS = 36


class TextProcessing:
    """Methods to work with text."""
    @staticmethod
    def remove_whitespace(text: str) -> str:
        """remove all unneccessary whitespace"""
        text = text.replace('\n', ' ')
        text = text.replace('\u3000', ' ')
        text = re.sub(r'[ ]+', ' ', text)
        return text

    @staticmethod
    def replace_punctuation_signs(text: str) -> str:
        """Replace symbols such as apostrophe, ampersand, angle brackets with words."""
        REPLACE = {
            r"&
