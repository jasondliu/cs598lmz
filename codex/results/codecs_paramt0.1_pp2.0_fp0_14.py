import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_list(filename):
    return get_file_contents(filename).split('\n')

def get_file_contents_as_dict(filename):
    return dict(line.split('=') for line in get_file_contents_as_list(filename))

def get_file_contents_as_list_of_dicts(filename):
    return [dict(line.split('=') for line in line_list) for line_list in [line.split(';') for line in get_file_contents_as_list(filename)]]

def get_file_contents_as_list_of_lists
