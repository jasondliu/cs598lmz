from _struct import Struct
s = Struct.__new__(Struct)

if opts.pack:
    s.error = lambda *a, **kv: None
    s.format = opts.fmt
    try:
        print repr(s.pack(*map(lambda c: int(c, 0), args)))
    except:
        sys.exit(1)
    
else:
    if len(args) != len(opts.fmt):
        parser.error("Not enough arguments for the format")
    s.format = opts.fmt
    try:
        print s.unpack(args[0]),
    except:
        sys.exit(1)
