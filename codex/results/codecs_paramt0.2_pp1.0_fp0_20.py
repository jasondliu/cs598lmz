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

def get_file_list_by_ext_and_keyword(path, ext, keyword):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext) and keyword in file:
                file_list.append(os.path.join(root, file))
    return file_list

def get
