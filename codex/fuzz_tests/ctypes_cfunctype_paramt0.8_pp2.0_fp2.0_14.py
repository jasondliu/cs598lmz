import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None) #Change this if the need arises

def run(path, entries, int_size, string_size):
    for name, entry in entries.items():
        if name.endswith('.h'):
            name = name.rstrip('.h')
            continue #skip headers
        name = name.rstrip('.c')
        if ctypes.CDLL(path + "/_%s.so" % name).__getattr__(name) != None:
            continue #skip already linked modules
        sofile = ctypes.CDLL('%s/%s.so' % (path, name))
        for entry in entry:
            if (not entry.endswith('.h')) and (not entry.endswith('.c')):
                sofile.__getattr__(entry).argtypes = [ctypes.c_int] * int_size
                sofile.__getattr__(entry).argtypes += [ctypes.c_char_p] * string_size
                sofile.__getattr__(entry).restype = ctypes.c_
