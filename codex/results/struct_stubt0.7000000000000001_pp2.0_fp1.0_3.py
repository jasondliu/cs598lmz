from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', '<I')
s.size = s.__sizeof__()
s.pack = s.__call__
s.unpack = lambda b: (s.unpack_from(b, 0)[0], b[s.size:])
s.unpack_from = s.unpack_from

def pack(data):
    if type(data) is int:
        return s.pack(data)
    else:
        return b''.join(map(s.pack, data))

def unpack(data):
    res = []
    while data:
        res.append(s.unpack(data)[0])
        data = data[s.size:]
    return res

def unpack_from(data, offset):
    return s.unpack_from(data, offset)[0]

def sizeof():
    return s.size

# ------------------------------------------------------------------------------

def main():
    # Create a memory image from mem.img
    memory = create_mem_image("mem.img")

    # Get the base address of the
