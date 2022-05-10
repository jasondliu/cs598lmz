import codecs
# Test codecs.register_error, bug #1268574
codecs.register_error('e', codecs.ignore_errors)

# Test that the null character can be decoded in text mode
open(TESTFN, "w").write("\0")
f = open(TESTFN, "r")
g = codecs.getreader("ascii")(f)
g.read()
f.close()

# Test that the utf-16 codecs work
# test the BOM
for enc in 'utf-16', 'utf-16-le', 'utf-16-be':
    f = open(TESTFN, "w")
    f.write(u'\ufeffpi: \u03c0\n').encode(enc)
    f.close()
    f = open(TESTFN, "r")
    g = codecs.getreader(enc)(f)
    s = g.read()
    f.close()
    if s != u'\ufeffpi: \u03c0\n':
        raise TestFailed('%s BOM encoding failed' %
