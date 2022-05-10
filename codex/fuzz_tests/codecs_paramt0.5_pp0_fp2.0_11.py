import codecs
codecs.register_error('strict', codecs.ignore_errors)

# A simple wrapper to make sure that the output directory exists
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    return f

# Similar to ensure_dir, but makes sure the directory is empty
def ensure_empty_dir(d):
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    return d

# A simple wrapper to open a file with the specified codec
def open_file(filename, mode, encoding='utf-8'):
    return codecs.open(filename, mode, encoding=encoding)

# A simple wrapper to read a text file
def read_file(filename, encoding='utf-8'):
    with open_file(filename, 'r', encoding) as f:
        return f.read()

# A simple wrapper to write to a text file
def write_file(filename, text,
