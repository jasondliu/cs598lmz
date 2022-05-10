import codecs
codecs.register_error('strict', codecs.ignore_errors)

# -----------------------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------------------

def read_file(filename):
    """Read a file and return its contents as a string."""
    with open(filename, 'rb') as f:
        return f.read().decode('utf-8', 'strict')

def write_file(filename, contents):
    """Write a string to a file."""
    with open(filename, 'wb') as f:
        f.write(contents.encode('utf-8'))

# -----------------------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------------------

def get_header_from_file(filename):
    """Extract the header from a file."""
    contents = read_file(filename)
    lines = contents.splitlines()
    header = []
    for line in lines:
        if line.startswith('#'):
            header.append(line)
        else:
            break
    return '\n'.join(header)

def get_header_from_string(contents):
