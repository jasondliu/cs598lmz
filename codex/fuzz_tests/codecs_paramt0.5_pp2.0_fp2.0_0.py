import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    with open(filename) as f:
        return f.read()

def get_file_contents_utf8(filename):
    return get_file_contents(filename).decode('utf-8', 'strict')

def get_file_contents_cp1251(filename):
    return get_file_contents(filename).decode('cp1251', 'strict')

def get_file_contents_cp866(filename):
    return get_file_contents(filename).decode('cp866', 'strict')

def get_file_contents_koi8r(filename):
    return get_file_contents(filename).decode('koi8-r', 'strict')

def get_file_contents_koi8u(filename):
    return get_file_contents(filename).decode('koi8-u', 'strict')

def get_file_contents_iso8859_5(filename):
