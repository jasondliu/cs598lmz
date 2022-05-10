from _struct import Struct
s = Struct.__new__(Struct)

if opts.pack:
    s.error = lambda *a, **kv: None
    s.format = opts.fmt
