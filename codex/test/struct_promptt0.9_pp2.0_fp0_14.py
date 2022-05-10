import _struct
# Test _struct.Struct.format_size()
with support.cleandir() as dir:
    filename = os.path.join(dir, 'name')
    with open(filename, 'wb') as f:
        pass
    os.write(os.open(filename, os.O_WRONLY), b'a')
    s = _struct.Struct('b')
    with open(filename, 'rb') as f:
        size = s.format_size(f)
    s = _struct.Struct('b')
    with open(filename, 'wb') as f:
        s.pack_into(f, 0, 1)
    with open(filename, 'r+') as f:
        size = s.format_size(f)
# Test _struct.Struct.calcsize()
with support.cleandir() as dir:
    filename = os.path.join(dir, 'name')
    with open(filename, 'wb') as f:
        pass
    os.write(os.open(filename, os.O_WRONLY), b'a')
