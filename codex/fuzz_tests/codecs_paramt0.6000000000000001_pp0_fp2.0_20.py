import codecs
codecs.register_error("strict", codecs.ignore_errors)

def __get_categories(path):
    categories = []
    for d in os.listdir(path):
        if os.path.isdir(path + "/" + d):
            categories.append(d)
    return categories

def __get_files(path):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(path + "/" + f):
            files.append(f)
    return files

def read_file(filename):
    f = codecs.open(filename, 'r', encoding="utf-8", errors="strict")
    file_content = f.read()
    f.close()
    return file_content

def __read_files(path):
    files = __get_files(path)
    data = []
    for f in files:
        content = read_file(path + "/" + f)
        data.append(content)
    return data

def load_dataset(path):
    categories = __
