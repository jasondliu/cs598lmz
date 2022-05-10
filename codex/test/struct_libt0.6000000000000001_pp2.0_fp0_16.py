import _struct
import array

def analyze_struct(s):
    t = type(s)
    if hasattr(s, '__format__'):
        return s.__format__()
    if t == _struct.Struct:
        return s.format
    if t == _struct.StructType:
        return s.format_char
    if t == _struct.error:
        return str(s)
    return 'unknown type %s' % t

def analyze_array(a):
    return (a.typecode, len(a))

def analyze_string(s):
    return len(s)

def analyze_unicode(s):
    return len(s)

def analyze_buffer(s):
    return len(s)

def analyze_memoryview(s):
    return (s.format, s.nbytes)

def analyze_object(o):
    return type(o)

def analyze_dict(d):
    return len(d)

def analyze_list(l):
    return len(l)

