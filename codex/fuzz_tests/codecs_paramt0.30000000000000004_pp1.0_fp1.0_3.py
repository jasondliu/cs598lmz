import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(file_name):
    f = codecs.open(file_name, 'r', 'utf-8', 'replace_with_space')
    file_contents = f.read()
    f.close()
    return file_contents

def write_file(file_name, file_contents):
    f = codecs.open(file_name, 'w', 'utf-8')
    f.write(file_contents)
    f.close()

def get_files(dir_name):
    files = os.listdir(dir_name)
    return files

def get_file_paths(dir_name):
    file_paths = []
    files = os.listdir(dir_name)
    for file in files:
        file_path = os.path.join(dir_name, file)
        file_paths.append(file_path)
    return file_paths

def get_file_contents(dir_name):

