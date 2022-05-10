import codecs
codecs.register_error('ignore', lambda x: u'')

def unicode2str(str_):
    return unicode(str_).encode('utf-8', 'ignore')

def str2unicode(unicode_):
    return unicode(unicode_, 'utf-8', 'ignore')

def is_assci(chr_):
    return ord(chr_) > 0 and ord(chr_) < 127

def is_number(chr_):
    return ord(chr_) >= ord('0') and ord(chr_) <= ord('9')

def is_letter(chr_):
    return ord(chr_) >= ord('a') and ord(chr_) <= ord('z') or \
           ord(chr_) >= ord('A') and ord(chr_) <= ord('Z')

def is_space(chr_):
    return chr_ == ' ' or chr_ == '\t' or chr_ == '\n'

def is_eof(chr_):
    return ch
