import bz2
# Test BZ2Decompressor.__init__()
# Test that when the argument is invalid, TypeError is raised
# with a message that contains the name of the method.
b = bz2.BZ2Decompressor(1)
try:
    b.decompress(b'x')
except Exception as e:
    if (type(e) is not TypeError or
        bz2.__name__ not in str(e) or
        "decompress" not in str(e) or
        str(e) == "must be string or buffer, not int"):
        print("ERROR: expected TypeError with a message that contains " +\
              "'decompress'", file=sys.stderr)
        if str(e) != "must be string or buffer, not int":
            print("ERROR: instead got %r" % e, file=sys.stderr)
