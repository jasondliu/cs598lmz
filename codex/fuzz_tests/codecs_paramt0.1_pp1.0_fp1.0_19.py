import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_list(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read().splitlines()

def get_file_contents_as_list_of_lists(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return [line.split() for line in f.read().splitlines()]

def get_file_contents_as_list_of_lists_of_lists(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return [[word.split('_') for word in line.split()] for line in f.read().splitlines()]

def get_file_cont
