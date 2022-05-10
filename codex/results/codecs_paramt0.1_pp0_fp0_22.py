import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def get_file_contents(file_name):
    with codecs.open(get_file_path(file_name), 'r', 'utf-8') as f:
        return f.read()

def get_file_contents_as_list(file_name):
    with codecs.open(get_file_path(file_name), 'r', 'utf-8') as f:
        return f.read().splitlines()

def get_file_contents_as_dict(file_name):
    with codecs.open(get_file_path(file_name), 'r', 'utf-8') as f:
        return dict(line.strip().split('\t') for line in f)

def get_file_contents_as_dict_list(file_name):
    with codecs.open(get_file_path(file
