import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_lines(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def write_file_content(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def write_file_content_lines(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.writelines(content)

def get_file_content_lines_as_list(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return [line.strip() for line in f.readlines()]


