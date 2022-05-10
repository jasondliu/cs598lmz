import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

def find_files(path, ext):
    """Find all files in path with extension ext"""
    return glob.glob(os.path.join(path, '*' + ext))

def read_file(filename):
    """Read a file and return its contents."""
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, contents):
    """Write the given contents to a text file."""
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(contents)

def read_lines(filename):
    """Read a file and return a list of lines."""
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.readlines()

def write_lines(filename, contents):
    """Write the given contents to a text file."""
