import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def read_file(path):
    with open(path, 'r', encoding='utf-8', errors='surrogateescape') as file:
        return file.read()

def write_file(path, contents):
    with open(path, 'w', encoding='utf-8', errors='surrogateescape') as file:
        file.write(contents)

def read_lines(path):
    with open(path, 'r', encoding='utf-8', errors='surrogateescape') as file:
        return file.readlines()

def write_lines(path, lines):
    with open(path, 'w', encoding='utf-8', errors='surrogateescape') as file:
        file.writelines(lines)

def append_file(path, contents):
    with open(path, 'a', encoding='utf-8', errors='surrogateescape') as file:
        file.write(contents)

def append_lines(path, lines):
    with open(
