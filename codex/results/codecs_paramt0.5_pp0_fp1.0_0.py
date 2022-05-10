import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_list(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        return [line.strip() for line in f]

def get_dict(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        return dict((line.strip().split('\t')[0], line.strip().split('\t')[1]) for line in f)

def get_dict_list(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        return dict((line.strip().split('\t')[0], line.strip().split('\t')[1:]) for line in f)

def get_dict_set(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        return dict((line.strip().split('\t')[0], set(line.strip().split('\t')[1:])) for line in f)


