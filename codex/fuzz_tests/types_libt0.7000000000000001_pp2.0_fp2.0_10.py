import types
types.MethodType = types.FunctionType

def get_path(file_name):
    return os.path.join(os.path.dirname(file_name), '../package/')

def get_name(file_name):
    return os.path.splitext(os.path.basename(file_name))[0]

def get_header(file_name):
    return get_name(file_name) + '.h'

def get_source(file_name):
    return get_name(file_name) + '.cpp'

def to_camel(s):
    return ''.join(x.capitalize() or '_' for x in s.split('_'))

def to_lower_camel(s):
    return s[0].lower() + to_camel(s)[1:]

def to_upper_camel(s):
    return s[0].upper() + to_camel(s)[1:]

def to_path(s):
    return s.replace('_', '/')

def to_sy
