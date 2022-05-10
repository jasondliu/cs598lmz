import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(file_name):
    with codecs.open(file_name, 'r', 'utf8', 'replace_with_space') as f:
        return f.read()

def write_file(file_name, text):
    with codecs.open(file_name, 'w', 'utf8') as f:
        f.write(text)

def get_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_files_by_ext(path, ext):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                file_list.append(os.path.join(root, file))
    return file_list

def get_files_
