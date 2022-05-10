import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

class Text_Processing():
    def __init__(self, text_path):
        self.text_path = text_path
        self.text_name = os.path.basename(text_path)
        self.text_dir = os.path.dirname(text_path)
        self.text_content = self.read_text()
        self.text_content_cleaned = self.clean_text()
        self.text_tokenized = self.tokenize_text()
        self.text_stemmed = self.stem_text()
        self.text_lemmatized = self.lemmatize_text()
        self.text_pos_tagged = self.POS_tag_text()
        self.text_chunked = self.chunk_text()
        self.text_chunked_cleaned = self.clean_chunked_text()
        self.text_chunked_cleaned_stemmed = self.
