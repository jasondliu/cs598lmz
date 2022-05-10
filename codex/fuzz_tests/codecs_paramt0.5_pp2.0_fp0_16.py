import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_file_content(filepath):
    with codecs.open(filepath, 'r', 'utf-8', 'ignore') as f:
        return f.read()

def write_file(filepath, content):
    with codecs.open(filepath, 'w', 'utf-8', 'ignore') as f:
        f.write(content)

def get_file_extension(filepath):
    return os.path.splitext(filepath)[1]

def get_file_name(filepath):
    return os.path.basename(filepath)

def get_file_name_without_extension(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def get_file_size(filepath):
    return os.path.getsize(filepath)

def get_file_modification_time(filepath):
    return os.path.getmtime(filepath)

def get_file_creation
