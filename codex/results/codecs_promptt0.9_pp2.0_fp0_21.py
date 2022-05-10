import codecs
# Test codecs.register_error('ignore') to suppress "UnicodeEncodeError:
# 'ascii' codec can't encode character in position 0: ordinal not in
# range(128)"
def get_fieldnames(worksheet):
    fields = [u'original_name', u'code', u'original_account', u'account',
              u'original_char_1', u'char_1',
              u'original_char_2', u'char_2',
              u'original_char_3', u'char_3',
              u'original_char_4', u'char_4',
              u'original_char_5', u'char_5',
              u'original_char_6', u'char_6',
              u'original_char_7', u'char_7',
              u'original_char_8', u'char_8',
              u'original_char_9', u'char_9',
              u'original_char_10', u'char_10',
              u'original_char_11', u'char_11',
              u'original
