import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import os

def open_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None


def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


def get_file_list(dirname):
    return os.listdir(dirname)


def get_file_ext(filename):
    return os.path.splitext(filename)[-1]


def get_file_dir(filename):
    return os.path.dirname(filename)


def get_file_name(filename):
    return os.path.basename(filename)


def get_file_name_no_ext(filename):
    return os.path.splitext(os.path.basename(filename))[
