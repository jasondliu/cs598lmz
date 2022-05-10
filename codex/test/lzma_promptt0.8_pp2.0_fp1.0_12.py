import lzma
# Test LZMADecompressor
def _check_lzma_decompressor(data, fmt, check, check_args=None, check_kwargs=None,
                             filters=None,
                             filter_decode=None, filter_decode_args=None, filter_decode_kwargs=None,
                             filter_name=None, filter_flags=None,
                             filter_properties_size=None, filter_properties=None):
    if fmt != FORMAT_XZ:
        return
    if data[0:6] != b"\xFD7zXZ\x00":
        raise TestError("Bad header")
    if len(data) >= 12:
        if data[6:12] != b"\xFF\xFF\xFF\xFF\xFF\xFF":
            if len(data) < 12+6:
                raise TestError("Footer is too small")
            if data[-6:] != b"\x00\x00\x00\x00\x00\x00":
                raise TestError("Footer is not zeroed")
           
