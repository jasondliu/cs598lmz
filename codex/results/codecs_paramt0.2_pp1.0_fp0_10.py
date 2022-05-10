import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            file_list.append(os.path.join(root, f))
    return file_list

def get_file_list_by_ext(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                file_list.append(os.path.join(root, f))
    return file_list

def get_file_list_by_ext_list(path, ext_list):
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            for ext in ext_list:
                if f.endswith(ext):
                    file_list.append(os.path.join(root, f))
                    break
    return file_list
