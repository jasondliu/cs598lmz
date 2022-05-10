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
    content_list = []
    for file_path in file_path_list:
        content_list.append(get_file_content(file_path))
    return content_list

def get_file_content_list_with_label(file_path_list, label):
    content_list = []
    for file_path in file_path_list:
        content_list.append((get_file_content(file_path), label))
    return content_list

def
