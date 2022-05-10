import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_name(path):
    return os.path.basename(path)

def get_file_ext(path):
    return os.path.splitext(path)[1]

def get_file_path(path):
    return os.path.dirname(path)

def get_file_size(path):
    return os.path.getsize(path)

def get_file_mtime(path):
    return os.path.getmtime(path)

def get_file_ctime(path):
    return os.path.getctime(path)

def get_file_atime(path):
    return os.path.getatime(path)

def get_file_content(path
