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

def get_file_extension(path):
    return os.path.splitext(path)[1]

def get_file_name_without_extension(path):
    return os.path.splitext(path)[0]

def get_file_content(path):
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_without_bom(path):
    with codecs.open(path, 'r', 'utf-8-sig', 'strict') as f:
        return f.read()

def get_
