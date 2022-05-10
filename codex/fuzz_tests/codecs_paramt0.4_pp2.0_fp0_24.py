import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_content_with_newline(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        return f.read() + '\n'

def write_file_content(file_path, content):
    with codecs.open(file_path, 'w', encoding='utf-8', errors='strict') as f:
        f.write(content)

def append_file_content(file_path, content):
    with codecs.open(file_path, 'a', encoding='utf-8', errors='strict') as f:
        f.write(content)

def get_file_lines(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8
