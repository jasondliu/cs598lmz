import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_file_names(dir_path):
    files = [name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))]
    return files

def get_dir_names(dir_path):
    dirs = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]
    return dirs

def get_dir_file_names(dir_path):
    file_names = []
    dir_names = []

    for dirpath, dirnames, filenames in os.walk(dir_path):
        file_names.extend(filenames)
        dir_names.extend(dirnames)
       
