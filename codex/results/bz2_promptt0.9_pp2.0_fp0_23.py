import bz2
# Test BZ2Decompressor using a decompress_into method developed here
# to replicate the zlib decompress_into method for comparing and
# testing purposes.

def bz2decompress(data, maxlength):
    '''
    Replicates the behavior of BZ2Decompressor.decompress using a
    custom decompress_into method that mimics the zlib.decompress_into
    behavior.
    '''
    buf = []
    buf_len = 0
    while True:
        # If at least 1 byte is available in the current input buffer,
        # fill it up to the maxlength.
        buf_len = len(buf)
        if buf_len < maxlength:
            data_len = len(data)
            # Make sure the buffer is large enough to at least
            # read a header.
            if buf == []:
                buf = [0,] * 4
                if data_len < 4:
                    return b''.join(buf)
                else:
                    buf = [byte for byte in data[0:4]]
                    data = data[4:]
                    data_len
