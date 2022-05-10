import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_lines(filename):
    """
    Read text file and return a list of unicode strings.
    """
    lines = []
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)
    return lines

def write_lines(filename, lines, append=False):
    """
    Write a list of unicode strings to a text file.
    """
    with codecs.open(filename, 'a' if append else 'w', 'utf-8', 'strict') as f:
        for line in lines:
            f.write(line + u'\n')

def write_json(filename, data, append=False):
    """
    Write a list of unicode strings to a text file.
    """
    with codecs.open(filename, 'a' if append else 'w', 'utf-8', 'strict') as f:
       
