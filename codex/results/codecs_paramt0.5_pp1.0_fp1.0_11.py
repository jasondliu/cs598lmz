import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class File(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.file_size = os.path.getsize(self.file_path)
        self.file_type = None
        self.file_ext = self.file_name.split('.')[-1]
        self.file_text = None
        self.file_text_len = None
        self.file_text_lines = None
        self.file_text_words = None
        self.file_text_chars = None
        self.file_text_unique_words = None
        self.file_text_unique_chars = None
        self.file_text_unique_words_len = None
        self.file_text_unique_chars_len = None
        self.file_text_words_len = None
        self.file_text_chars_len = None
        self.
