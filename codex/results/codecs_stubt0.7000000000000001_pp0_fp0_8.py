import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# test utf-16
if os.path.isfile(TESTFN):
    os.remove(TESTFN)

f = codecs.open(TESTFN, "w+", "utf-16-le")
f.write("\u20ac\xff\u20ac")
f.seek(0)
buf = f.read()
if buf != "\u20ac\ufffd\u20ac":
    print("bad unicode result:", buf)
f.close()

f = codecs.open(TESTFN, "w+", "utf-16-be")
f.write("\u20ac\xff\u20ac")
f.seek(0)
buf = f.read()
if buf != "\u20ac\ufffd\u20ac":
    print("bad 
