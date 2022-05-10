import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_contents_as_list(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def get_file_contents_as_list_stripped(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return [line.strip() for line in f.readlines()]

def get_file_contents_as_list_stripped_nonempty(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def get_file_contents_as_list_stripped_nonempty_noncomment
