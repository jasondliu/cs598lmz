import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_file_paths(dir):
    file_paths = []
    for root, directories, files in os.walk(dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def read_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8', 'ignore') as f:
        return f.read()

def get_files_content(dir):
    file_paths = get_file_paths(dir)
    files_content = []
    for filepath in file_paths:
        files_content.append(read_file(filepath))
    return files_content

def get_files_content_by_category(dir):
    file_paths = get_file_paths(dir)
    files_content = {}
    for filepath in file_paths:
        category = filepath.split('/')[-
