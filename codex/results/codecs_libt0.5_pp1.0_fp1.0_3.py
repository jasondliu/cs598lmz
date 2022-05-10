import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#functions
def get_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_file_name(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_file_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_file_list(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.listdir(path)

def get_file_list_full(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return glob.glob(path)

def get_file_list_full_with_ext(path,ext):
    if not
