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

def get_file_content_by_line(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_name_no_ext(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def get_file_ext(file_path
