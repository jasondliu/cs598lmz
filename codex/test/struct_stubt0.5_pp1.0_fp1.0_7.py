from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format = '<3s3sHH'
s.unpack = Struct.unpack

def get(data, i):
    return s.unpack_from(data, i)

def get_color(data, i):
    c = s.unpack_from(data, i)
    return c[3], c[4]

def get_image_size(data):
    return get(data, 0)[1]

def get_color_table_size(data):
    return get(data, 10)[3]

def get_pixel_data_offset(data):
    return get(data, 10)[4]

def get_palette_color(data, i):
    return get_color(data, 54 + i * 4)

def get_pixel_color(data, i):
    return get_color(data, get_pixel_data_offset() + i * 2)
