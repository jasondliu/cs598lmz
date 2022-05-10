import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def read_file_latin1(filename):
    with open(filename, 'r', encoding='latin-1') as f:
        return f.read()

def read_file_ignore(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def read_file_replace(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def read_file_strict(filename):
    with open(filename, 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def read_file_backslashreplace(filename):
    with open(filename, 'r', encoding='utf-8', errors='backslashreplace') as f:
        return f.
