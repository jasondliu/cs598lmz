import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def read_file(filename):
    """Read a file and return its contents."""
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

#-------------------------------------------------------------------------------

def write_file(filename, contents):
    """Write a file with the given contents."""
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(contents)

#-------------------------------------------------------------------------------

def read_json_file(filename):
    """Read a JSON file and return its contents."""
    with open(filename) as f:
        return json.load(f)

#-------------------------------------------------------------------------------

def write_json_file(filename, contents):
    """Write a JSON file with the given contents."""
    with open(filename, 'w') as f:
        json.dump(contents, f, indent=2, sort_keys=True)

#-------------------------------------------------------------------------------

def read_y
