import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def get_file_content_with_ignore(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        content = f.read()
    return content

def get_file_content_with_ignore_and_replace(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    return content

def get_file_content_with_ignore_and_ignore(file_path):
