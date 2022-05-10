import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def get_file_path(file_path):
    return os.path.join(os.path.dirname(__file__), file_path)

def get_file_path_from_root(file_path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)

def get_file_path_from_parent(file_path):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), file_path)

def get_file_path_from_grandparent(file_path):
    return os.path.join(os.path
