from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
def get_short(f):
    return s.unpack(f.read(2))[0]


GUID = Struct('<i4sHHLQQQ')

# Unpack various stream header structures.  These contain the chunk headers
# for the chunks that follow.
def RT_UNKNOWN(flags): return GUID(flags)
def RT_CORE(flags): Pin(flags)
def RT_ARCHIVE(flags): ArchiveProps(flags)
def RT_USERDATA(flags): GUID(flags)
def RT_CLIPDATA(flags): GUID(flags)


def printf(*args):
    sys.stdout.write(''.join([str(arg) for arg in args]))
def print_int(i, base=None,fmt='%d'):
    if base is not None:
        print(fmt % (i,))
    printf('%d' % (i,))
def print_float(f):
    printf('%f' % (f,))
