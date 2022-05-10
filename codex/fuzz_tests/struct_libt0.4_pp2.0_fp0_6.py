import _struct

def read_int(f):
    return _struct.unpack('<i', f.read(4))[0]

def read_string(f):
    length = read_int(f)
    return f.read(length).decode('utf-8')

def read_float(f):
    return _struct.unpack('<f', f.read(4))[0]

def read_bool(f):
    return bool(_struct.unpack('<?', f.read(1))[0])

def read_bytes(f):
    length = read_int(f)
    return f.read(length)

def read_list(f, read_element):
    length = read_int(f)
    return [read_element(f) for i in range(length)]

def read_dict(f, read_key, read_value):
    length = read_int(f)
    return {read_key(f): read_value(f) for i in range(length)}

def read_object(f):
   
