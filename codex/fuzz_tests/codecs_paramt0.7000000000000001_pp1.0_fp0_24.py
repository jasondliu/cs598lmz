import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Sentence splitter class
class SentenceSplitter(object):
    def __init__(self):
        self.sentence_delimiters = re.compile(u'[.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
        self.phrase_delimiters = re.compile(u'[.!?,;:\t\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
    def split(self, text):
        sentences = [sentence for sentence in self.parse(text)]
        return sentences
        
    def parse(self, text):
        phrase_split_text = self.phrase_delimiters.split(text)
        for phrase in phrase_split_text:
            sentence_split_text = self.sentence_delimiters.split(phrase)
            for sentence in sentence_split_text:
                if sentence:
                    yield sentence.strip() + u'
