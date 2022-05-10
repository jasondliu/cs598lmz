import codecs
codecs.register_error('replace_spaces', lambda e: (u'\uFFFD', e.start + 1))

def get_text(filename):
    return codecs.open(filename, 'r', 'utf-8', 'replace_spaces').read()

def get_text_list(filename):
    return [line.strip() for line in codecs.open(filename, 'r', 'utf-8', 'replace_spaces')]

def get_text_dict(filename):
    return dict([line.strip().split('\t') for line in codecs.open(filename, 'r', 'utf-8', 'replace_spaces')])

def get_text_dict_list(filename):
    return [line.strip().split('\t') for line in codecs.open(filename, 'r', 'utf-8', 'replace_spaces')]

def get_text_dict_list_dict(filename):
    return [dict([line.strip().split('\t') for line in codecs.open(filename, 'r', 'utf-8', 'replace_spaces
