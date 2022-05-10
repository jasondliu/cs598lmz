import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_lines(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def write_file_content(file_path, content):
    with codecs.open(file_path, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def write_file_content_lines(file_path, content_lines):
    with codecs.open(file_path, 'w', 'utf-8', 'strict') as f:
        f.writelines(content_lines)

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_name_without_ext(file
