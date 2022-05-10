import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_lines(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def get_file_content_bytes(filename):
    with open(filename, 'rb') as f:
        return f.read()

def write_file_content(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def write_file_content_lines(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.writelines(content)

def write_file_content_bytes(filename, content):
    with open(filename, 'wb') as f:
