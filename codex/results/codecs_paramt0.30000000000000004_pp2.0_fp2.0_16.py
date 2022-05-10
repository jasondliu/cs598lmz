import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, contents):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(contents)

def get_file_list(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_file_list_recursive(path):
    files = []
    for root, subdirs, f in os.walk(path):
        for file in f:
            files.append(os.path.join(root, file))
    return files

def get_dir_list(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def get_dir
