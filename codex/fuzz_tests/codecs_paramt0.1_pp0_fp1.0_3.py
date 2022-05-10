import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
        return f.read()

def get_file_contents_as_bytes(filename):
    with open(get_file_path(filename), 'rb') as f:
        return f.read()

def get_file_contents_as_bytes_strict(filename):
    with codecs.open(get_file_path(filename), 'rb', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_bytes_ignore(filename):
    with codecs.open(get_file_path(filename), 'rb', 'utf-8', 'ignore') as f:
        return f.read()

def get_file_contents_as_
