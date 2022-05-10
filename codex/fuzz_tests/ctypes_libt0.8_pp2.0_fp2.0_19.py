import ctypes
ctypes._endian_ = 'big'

def C(typ):
    return ctypes.c_uint8 * typ

INFO_CHUNK_ID = 0x494E464F
INFO_CHUNK_SIZE = 0x02

def gen_header():
    header = io.BytesIO()
    header.write(b'RIFF')
    header.write(C(4)(0x7FFFFFFF))
    header.write(b'WAVE')
    header.write(C(4)(INFO_CHUNK_ID))
    header.write(C(4)(INFO_CHUNK_SIZE))
    return header

def gen_footer():
    footer = io.BytesIO()
    footer.write(b'fact')
    footer.write(C(4)(0x00000004))
    footer.write(C(4)(0x00000000))
    footer.write(b'data')
    footer.write(C(4)(0x7FFFFFFF))
    return footer

def gen_wave():
    wave = io
