import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        text = f.read()
    return text

def get_file_list(dirname):
    return [os.path.join(dirname, f) for f in os.listdir(dirname)]

def get_files_content(dirname):
    files = get_file_list(dirname)
    content = [read_file(f) for f in files]
    return content

def get_files_content_by_category(rootdir):
    dir_list = [os.path.join(rootdir, d) for d in os.listdir(rootdir)]
    category_list = [d.split('/')[-1] for d in dir_list]
    files_content = [get_files_content(d) for d in dir_list]
    return category_list, files_content

def get_category_id
