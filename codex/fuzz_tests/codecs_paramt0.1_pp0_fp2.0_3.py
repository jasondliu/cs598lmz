import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_contents_as_list(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='strict') as f:
        return f.read().splitlines()

def get_file_contents_as_dict(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='strict') as f:
        return dict(line.strip().split('=', 1) for line in f)

def get_file_contents_as_json(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='st
