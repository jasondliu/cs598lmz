import _struct
# _struct might be lowercased in some versions of Python


def unpack(fmt, data):
    "unpack() (defined in this module) uses 'H' for uint16 etc. rather than 'B'"

    if isinstance(fmt, bytes):
        fmt = fmt.decode('ascii')

    if isinstance(data, bytearray) and not isinstance(data, bytes):
        data = bytes(data)

    fmt = fmt.replace('uint16', 'H')
    fmt = fmt.replace('uint32', 'I')
    fmt = fmt.replace('uint64', 'Q')
    return struct.unpack(fmt, data)


def pack(fmt, *data):
    "pack() (defined in this module) uses 'H' for uint16 etc. rather than 'B'"

    if type(fmt) == str:
        fmt = fmt.encode('ascii')

    if len(data) == 1 and isinstance(data[0], tuple):
        data = data[0]

    fmt = fmt.decode
