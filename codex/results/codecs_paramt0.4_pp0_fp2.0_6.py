import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    try:
        with codecs.open(filename, 'r', 'utf-8') as f:
            return f.read()
    except:
        return None

def get_file_contents_strict(filename):
    try:
        with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
            return f.read()
    except:
        return None

def get_file_contents_binary(filename):
    try:
        with open(filename, 'rb') as f:
            return f.read()
    except:
        return None

def write_file_contents(filename, contents):
    try:
        with codecs.open(filename, 'w', 'utf-8') as f:
            f.write(contents)
        return True
    except:
        return False

def write_file_contents_binary(filename, contents):
    try:
        with open(filename, '
