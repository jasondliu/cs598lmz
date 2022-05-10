import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

def get_file_contents(file_name):
    with codecs.open(get_file_path(file_name), encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_contents_lines(file_name):
    with codecs.open(get_file_path(file_name), encoding='utf-8', errors='strict') as f:
        return f.readlines()

def write_file_contents(file_name, contents):
    with codecs.open(get_file_path(file_name), 'w', encoding='utf-8', errors='strict') as f:
        f.write(contents)

def write_file_contents_lines(file_name, contents):
    with codecs.open(get_file_path
