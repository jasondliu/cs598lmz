import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_content(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name_without_extension(file_path):
    return os.path.splitext(file_path)[0]

def get_file_path_without_extension(file_path):
    return os.path.splitext(file_path)[0]

def get_
