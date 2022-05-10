import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def get_file_path(dir, file_name, file_extension):
    return os.path.join(dir, file_name + file_extension)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    return os.path.splitext(file_path)[0]

def get_file_name_with_extension(file_path):
    return os.path.basename(file_path)

def get_dir_name(file_path):
    return os.path.dirname(file_path)

def get_dir_name_without_extension(file_path):
    return os.path.splitext(os.path.dirname(file_path))[0]

def get_current_file_name_without_extension():
    return os.path.splite
