import _struct
# Test _struct.Struct.pack_into()
import struct

def get_sample_bitmap(width, height):
    """ returns a sample BMP header and data, in the form of a bytes 
        object"""
    header = get_bmp_header(width, height)
    data = b'\xff' * (width * 3 + width % 4) * height
    return header + data

def get_bmp_header(width, height):
    """ returns a BMP header, in the form of a bytes object"""
    header_len_b = b'\x36\x00\x00\x00'
    offset_b = b'\x40\x00\x00\x00'
    width_b = struct.pack("<I", width)
    height_b = struct.pack("<I", height)
    planes_b = b'\x01\x00'
    bits_b = b'\x18\x00'
    compression_b = b'\x00\x00\x00\x00'
