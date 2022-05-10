import bz2
# Test BZ2Decompressor's ability to handle errors.
decomp = bz2.BZ2Decompressor()
b = decomp.decompress(b'BZh91AY&SY') # No errors raised
raise Exception('FAILED: Error not raised')
"""
    run_python(code, expected_err='FAILED: Error not raised')


def test_bz2_file_open():
    """
    bz2.BZ2File(name[, mode='r', buffering=0, compresslevel=9])

    Return an open file object for the named data stream. 'mode' can be
    'r' for reading (default), 'w' for overwriting, 'x' for exclusive creation,
    or 'a' for appending. These can equivalently be given as 'rb', 'wb', 'xb',
    and 'ab'. 'buffering' can be given as an integer to indicate a raw stream
    buffer size, if given zero, no buffering is done. 'compresslevel' can be a
    number between 1 and 9, indicating the level of compression to be used.

    """

