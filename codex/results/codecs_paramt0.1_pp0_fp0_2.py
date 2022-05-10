import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def get_file_contents(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_contents_lines(filename):
    with codecs.open(get_file_path(filename), encoding='utf-8', errors='strict') as f:
        return f.readlines()

def get_file_contents_lines_stripped(filename):
    return [line.strip() for line in get_file_contents_lines(filename)]

def get_file_contents_lines_stripped_nonempty(filename):
    return [line for line in get_file_contents_lines_stripped(filename) if line]

def get_file_contents_lines_stripped_nonempty_noncomment(filename):
    return [
