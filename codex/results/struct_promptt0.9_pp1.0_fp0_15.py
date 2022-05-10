import _struct
# Test _struct.Struct for byte order of 'c' format
tst_format = ['c', 'c', 'c']
tst_struct = _struct.Struct(','.join(tst_format))
tst_result = tst_struct.unpack_from(b'\x00\x01\x02\x03\x04')
expected = (_b('\x00'), _b('\x01'), _b('\x02'))
if tst_result != expected:
    c_big_endian = False
else:
    # Big endian format
    tst_format = [c+'#' for c in tst_format]
    tst_struct = _struct.Struct(','.join(tst_format))
    tst_result = tst_struct.unpack_from(b'\x00\x01\x02\x03\x04')
    expected = (_b('\x01'), _b('\x02'), _b('\x03'))
    if tst_result != expected:
        c_big_endian = False
   
