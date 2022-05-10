import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(file_name):
    with codecs.open(file_name, 'r', 'utf-8-sig') as f:
        return f.read()

def write_file(file_name, content):
    with codecs.open(file_name, 'w', 'utf-8') as f:
        f.write(content)

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_name_without_ext(file_path):
    return os.path.splitext(get_file_name(file_path))[0]

def get_file_ext(file_path):
    return os.path.splitext(get_file_name(file_path))[1]

def get_file_path_without_ext(file_path):
    return os.path.splitext(file_path)[0]

def get_file_path_without_ext_and_name(file
