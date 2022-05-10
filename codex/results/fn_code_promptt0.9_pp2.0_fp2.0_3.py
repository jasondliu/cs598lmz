fn = lambda: None
# Test fn.__code__ and fn.__globals__
#assert(hasattr(fn, "__code__"))
#assert(hasattr(fn.__code__, "__class__"))
#assert(fn.__code__.__class__ == code)
#assert(hasattr(fn, "__globals__"))
#assert(fn.__globals__ == globals())

# Test I/O operations.

seterr(all="ignore") # reporting errors is not supported
f = open(TESTFN, "w")
f.write("testing...\n")
f.close()
f = open(TESTFN, "r")
assert(f.read() == "testing...\n")
f.close()

assert(open(TESTFN, "a").write("hello\n"))
assert(open(TESTFN, "r").read() == "testing...\nhello\n")
unlink(TESTFN)

assert(open(TESTFN, "w").write("testing\nlinetwo\n"))
f.close()
assert(open(TEST
