import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re

def get_list_of_paths(directory):
    paths = []
    for (dirpath, dirnames, filenames) in walk(directory):
        paths.extend(join(dirpath, filename) for filename in filenames)
    return paths

def get_bad_paths(directory):
    return [path for path in get_list_of_paths(directory) if exists(path + '.undecoded')]

def get_decoded_path(path):
    return path + '.undecoded'

def decode(path):
    return codecs.open(path, 'r', 'utf-8', 'strict').read()

def encode(path, data):
    codecs.open(path, 'w', 'utf-8', 'replace').write(data)

def is_unicode(path):
    return isinstance(decode(path), unicode)

def decode_paths(paths):
    for path in paths:
        decode_path(path)
