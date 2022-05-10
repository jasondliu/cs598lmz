import codecs
codecs.register_error("strict", codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, "r", "utf8", "ignore") as f:
        return f.read()

def write_file(filename, content):
    with codecs.open(filename, "w", "utf8", "ignore") as f:
        f.write(content)

def read_json(filename):
    return json.loads(read_file(filename))

def write_json(filename, content):
    write_file(filename, json.dumps(content))

def get_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            all_files.append(os.path.join(root, f))
    return all_files

def get_dirs(path):
    all_dirs = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            all_dirs.append(os.
