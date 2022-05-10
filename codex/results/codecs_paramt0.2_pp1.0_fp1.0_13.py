import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def get_text_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().split('\n')

def get_text_list_strict(filename):
    with open(filename, 'r', encoding='utf-8', errors='strict') as f:
        return f.read().split('\n')

def get_text_list_ignore(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read().split('\n')

def get_text_list_replace(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        return f.read().split('\n')

def get_text_list_xmlcharrefreplace(filename):
    with open(filename
