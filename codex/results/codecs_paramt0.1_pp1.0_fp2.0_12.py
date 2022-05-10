import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
        return f.read()

def get_file_contents_as_list(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
        return f.readlines()

def get_file_contents_as_list_of_lists(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
        return [line.split() for line in f.readlines()]

def get_file_contents_as_list_of_lists_of_lists(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8') as f:
