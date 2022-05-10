import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def get_file_contents(file_name):
    with codecs.open(get_file_path(file_name), 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_contents_and_close(file_name):
    with codecs.open(get_file_path(file_name), 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_contents_as_list(file_name):
    with codecs.open(get_file_path(file_name), 'r', encoding='utf-8', errors='strict') as f:
        return f.readlines()

def get_file_contents_as_list_and_close(file_name):
    with codecs.open(get
