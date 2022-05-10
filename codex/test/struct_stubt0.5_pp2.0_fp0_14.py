from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'QQQQ'
s.size = s.calcsize(s.format)

def write_struct(f, *values):
    f.write(s.pack(*values))

def read_struct(f):
    return s.unpack(f.read(s.size))

def write_file(f, name, contents):
    write_struct(f, 0, len(name), len(contents), 0)
    f.write(name)
    f.write(contents)

def write_header(f, nfiles):
    write_struct(f, 0xC0DA1E5E, 0, 0, nfiles)

def write_tar(f, files):
    offset = s.size + (s.size * len(files))
    write_header(f, len(files))
    for name, contents in files:
        write_file(f, name, contents)
        offset += s.size + len(name) + len(contents)
    f.seek(0)
    write_header
