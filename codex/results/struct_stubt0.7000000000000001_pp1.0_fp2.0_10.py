from _struct import Struct
s = Struct.__new__(Struct)
unpack = s.unpack

def parse(data):
    '''Parse the given data into a list of (offset, tag) tuples.'''
    tags = []
    if not data:
        return tags
    # The TAGs are at an offset of 0x800 from the start of the file.
    offset = 0x800
    # TAGs are 0x24 bytes long.
    length = 0x24
    # The number of TAGs is the first integer in the file.
    count = unpack('<I', data[:4])[0]
    # Loop over the TAGs.
    for i in range(count):
        # The file is split into chunks of 0x4000 bytes.
        chunk_num, chunk_offset = divmod(offset, 0x4000)
        chunk = data[chunk_num * 0x4000 : (chunk_num + 1) * 0x4000]
        # Each TAG is 0x24 bytes long.
        tag = chunk[chunk_offset : chunk_offset + length]
        # The first integer in each TAG is the hash of
