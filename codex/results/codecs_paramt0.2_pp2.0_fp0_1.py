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

def get_file_content_list(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def write_file_content(file_path, content):
    with codecs.open(file_path, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def write_file_content_list(file_path, content_list):
    with codecs.open(file_path, 'w
