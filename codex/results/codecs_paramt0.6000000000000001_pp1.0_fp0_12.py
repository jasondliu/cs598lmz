import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_files(path):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            yield entry

def find_files(path, pattern):
    for entry in get_files(path):
        if pattern.match(entry):
            yield entry

def find_files_in_dir(path, pattern):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            if pattern.match(entry):
                yield entry

def find_files_in_dir_recursive(path, pattern):
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)

def file_exists(file):
    return os.path.isfile(file)

def is_dir_exists(dir):
    return os
