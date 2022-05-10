import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='replace_with_space') as f:
        return f.read()

def write_file(filename, content):
    with codecs.open(filename, 'w', encoding='utf-8', errors='replace_with_space') as f:
        return f.write(content)

def read_file_lines(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='replace_with_space') as f:
        return f.readlines()

def write_file_lines(filename, lines):
    with codecs.open(filename, 'w', encoding='utf-8', errors='replace_with_space') as f:
        return f.writelines(lines)

def list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os
