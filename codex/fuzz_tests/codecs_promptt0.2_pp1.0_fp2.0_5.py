import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

def bad_translate(input, errors='strict'):
    raise UnicodeTranslateError(input, 0, 1, "bad")

def bad_recoder(input, errors='strict'):
    raise UnicodeError("bad")

def bad_reader(input, errors='strict'):
    raise UnicodeError("bad")

def bad_writer(input, errors='strict'):
    raise UnicodeError("bad")

def bad_streamreader(input, errors='strict'):
    raise UnicodeError("bad")

def bad_streamwriter(input, errors='strict'):
    raise UnicodeError("bad")

def bad_streamreaderwriter(input, errors='strict'):
    raise UnicodeError("bad")

def bad_incrementalencoder
