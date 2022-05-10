import codecs
codecs.register_error('strict', codecs.ignore_errors)

class NoopPreprocessor(Preprocessor):
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def __call__(self, text):
        return text

    def __repr__(self):
        return '<NoopPreprocessor>'

class LowercasePreprocessor(Preprocessor):
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def __call__(self, text):
        return text.lower()

    def __repr__(self):
        return '<LowercasePreprocessor>'

class StripAndLowercasePreprocessor(Preprocessor):
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def __call__(self, text):
        return text.strip().lower()

    def __repr__(self):
        return '<StripAndLowercasePreprocessor>'

class RegexPreprocessor(Preprocessor):
    def __init__(self
