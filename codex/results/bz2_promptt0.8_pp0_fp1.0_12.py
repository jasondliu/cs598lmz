import bz2
# Test BZ2Decompressor failed.
#
# Bad stream.
decomp = bz2.BZ2Decompressor()
try: raise EOFError()
except:
    try: decomp.decompress(b"\x42\x5a\x68")
    except EOFError: pass
    else: raise TestFailed("EOF expected")

# Bad magic number.
decomp = bz2.BZ2Decompressor()
try: raise EOFError()
except:
    try: decomp.decompress(b"\x43\x5a\x68")
    except IOError: pass
    else: raise TestFailed("IOError expected")

# Bad block header.
decomp = bz2.BZ2Decompressor()
try: raise EOFError()
except:
    try: decomp.decompress(b"\x42\x5a\x68\x39\x00\x00")
    except IOError: pass
    else: raise TestFailed("IOError expected")

# Bad block header CRC.
decomp = bz2.
