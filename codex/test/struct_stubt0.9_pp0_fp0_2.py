from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda : 100
s.format = lambda : ""
s.unpack = lambda x : []
s.getName = lambda : ""
    
    
    
    
    
def get_b64_stream(path):
    with open(path, "rb") as fh:
        b64_data = base64.b64encode(fh.read())
        new_data = str.replace(b64_data.decode("utf-8"), "\n", "")
    return new_data


def get_class_members(klass):  # pragma: no cover
    ret = dir(klass)
    if hasattr(klass, '__bases__'):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret

