import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    """
    Read a file and return its contents.
    """
    f = codecs.open(filename, 'r', 'utf-8', 'strict')
    content = f.read()
    f.close()
    return content

def write_file(filename, content):
    """
    Write the given content in a file.
    """
    f = codecs.open(filename, 'w', 'utf-8', 'strict')
    f.write(content)
    f.close()

def read_file_lines(filename):
    """
    Read a file and return its lines.
    """
    f = codecs.open(filename, 'r', 'utf-8', 'strict')
    lines = f.readlines()
    f.close()
    return lines

def write_file_lines(filename, lines):
    """
    Write the given lines in a file.
    """
    f = codecs.open(filename, 'w', 'utf-
