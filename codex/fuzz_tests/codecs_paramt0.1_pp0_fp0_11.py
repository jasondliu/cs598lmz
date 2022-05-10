import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
        return f.read()

def get_file_contents_binary(filename):
    with open(get_file_path(filename), 'rb') as f:
        return f.read()

def get_file_contents_strict(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_strict_binary(filename):
    with open(get_file_path(filename), 'rb', 'strict') as f:
        return f.read()

def get_file_contents_strict_binary_ignore(filename):
    with open(get_
