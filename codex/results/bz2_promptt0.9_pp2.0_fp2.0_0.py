import bz2
# Test BZ2Decompressor. If a short string is decompressed, the result is longer or equal
# if the sting failed to decompress, compressionType will be 'N/A', 
# and the decompressed string will be the original string.
def trybz2decompress( s, compressionType ):
    try:
        bz2comp = bz2.BZ2Compressor()
        compressed = bz2comp.compress( s )
        bz2decomp = bz2.BZ2Decompressor()
        endstate = bz2comp.flush()
        uncompressed = bz2decomp.decompress( compressed + endstate )
        if len(uncompressed) >= len( s ):
            return (compressionType, uncompressed)
        else:
            return (compressionType, uncompressed + bz2decomp.decompress( bz2decomp.unused_data ))
    except:
        return ('N/A', s)

def try_decompress( s ):
    strings = [s]
    # Test Snappy Decompress
    strings.append
