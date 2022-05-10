from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = s.calcsize(s.format)
s.unpack_from = s.unpack_from
s.pack = s.pack
s.pack_into = s.pack_into
s.unpack = s.unpack
s.unpack_from = s.unpack_from
s.iter_unpack = s.iter_unpack
s.iter_unpack_from = s.iter_unpack_from

def _read_exif_ifd(fp, offset, endian, parent_offsets, tag_dict, ifd_name):
    fp.seek(offset)
    num_entries = read_int(fp, 2, endian)
    for i in range(num_entries):
        tag = read_int(fp, 2, endian)
        type_ = read_int(fp, 2, endian)
        count = read_int(fp, 4, endian)
        if count == 0:
            continue
        type_size = TYPE_SI
