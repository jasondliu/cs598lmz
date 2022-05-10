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

def get_file_content_list(file_list):
    content_list = []
    for file in file_list:
        content_list.append(get_file_content(file))
    return content_list

def get_file_content_list_with_path(file_list):
    content_list = []
    for file in file_list:
        content_list.append((file, get_file_content(file)))
    return content_list

def get_file_content_list_with_path_and_label(file_
