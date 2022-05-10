import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def get_file_contents(file_name):
    file_path = get_file_path(file_name)
    with open(file_path, 'r') as f:
        return f.read()

def get_file_contents_utf8(file_name):
    file_path = get_file_path(file_name)
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_list(file_name):
    file_path = get_file_path(file_name)
    with open(file_path, 'r') as f:
        return f.readlines()

def get_file_contents_as_list_utf8(file_name):
    file_path = get_file_path
