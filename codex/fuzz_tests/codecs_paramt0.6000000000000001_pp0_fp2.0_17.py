import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
#
#
#
def read_file_as_set(filename):
    """
    Reads a file and returns the content as a set of lines.
    """
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        s = set([line.strip() for line in f])
    return s

def read_file_as_list(filename):
    """
    Reads a file and returns the content as a list of lines.
    """
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        s = [line.strip() for line in f]
    return s

def write_set_to_file(s, filename):
    """
    Writes a set of strings to a file, one per line.
    """
    with codecs.open(filename, 'w', 'utf-8') as f:
        for line in s:
            f.write(line
