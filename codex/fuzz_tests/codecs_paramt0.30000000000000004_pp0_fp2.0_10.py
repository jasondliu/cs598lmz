import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(data)

def get_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_dirs(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def get_files_recursive(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def
