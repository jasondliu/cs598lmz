import bz2
# Test BZ2Decompressor failed.
#
# Bad stream.
decomp = bz2.BZ2Decompressor()
try: raise EOFError()
except:
    try: decomp.decompress(b"\x42\x5a\x68")
    except EOFError: pass
