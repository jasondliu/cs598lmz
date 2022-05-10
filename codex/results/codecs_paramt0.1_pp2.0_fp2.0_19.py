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

def get_file_content_list(file_path_list):
    return [get_file_content(file_path) for file_path in file_path_list]

def get_file_content_list_by_path(path):
    return get_file_content_list(get_file_list(path))

def get_file_content_list_by_path_list(path_list):
    return [get_file_content_list_by_path(path) for path in path_list]

def get_file_content_
