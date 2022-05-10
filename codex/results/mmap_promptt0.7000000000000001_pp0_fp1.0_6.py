import mmap
# Test mmap.mmap.  Use a function to avoid leaving a file lying around.
def test_mmap():
    f = open(test.support.TESTFN, "w+b")
    try:
        f.write(b"\0" * 1024)
        f.flush()
        m = mmap.mmap(f.fileno(), 1024)
        m[0]
        m[0:1]
        m.rfind(b'\0')
        m.rfind(b'\0', 0, 1024)
        m.rfind(b'\0', 0, 10)
        m.rfind(b'\0', 0, 5)
        m.rfind(b'\0', 510, 511)
        m.rfind(b'\0', 511, 512)
        m.rfind(b'\0', 511)
        m.rfind(b'\0', 512)
        m.rfind(b'\0', 513)
        m.rfind(b'\0', 512, 513)
        m.rfind
