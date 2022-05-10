import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class FileObject(object):
    def __init__(self, fp):
        """
        fp: file pointer
        """
        self.fp = fp
        self.line_offset = []
        self.byte_offset = []
        self.line_num = 0
        self.token_num = 0
        self.word_num = 0
        self.byte_num = 0
        self.char_num = 0
        self.sentence_num = 0
        self.offset_num = 0
        self.offset_mapping = [] # (char_begin, char_end, token_begin, token_end)
        self.last_line = '' # last line
        self.last_token = '' # last token
        self.last_word = '' # last word
        self.last_byte = '' # last byte
        self.last_char = '' # last char
        self.last_sentence = '' # last sentence
        self.last_offset = '' # last offset
        self.
