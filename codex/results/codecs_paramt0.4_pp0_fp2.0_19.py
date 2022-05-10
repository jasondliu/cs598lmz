import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _read_file(file_path, encoding='utf-8'):
    with codecs.open(file_path, 'r', encoding=encoding, errors='strict') as f:
        return f.read()

def _read_file_lines(file_path, encoding='utf-8'):
    with codecs.open(file_path, 'r', encoding=encoding, errors='strict') as f:
        return f.readlines()

def _write_file(file_path, content, encoding='utf-8'):
    with codecs.open(file_path, 'w', encoding=encoding, errors='strict') as f:
        f.write(content)

def _write_file_lines(file_path, content, encoding='utf-8'):
    with codecs.open(file_path, 'w', encoding=encoding, errors='strict') as f:
        f.writelines(content)

def _get_files_recursively(root_dir):

