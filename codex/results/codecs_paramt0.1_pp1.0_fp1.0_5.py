import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_list_by_ext(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                file_list.append(os.path.join(root, file))
    return file_list

def get_file_list_by_ext_exclude(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(ext):
                file_list.append(os.path.join(root, file))
    return file_list

def get_file_list_by_ext
