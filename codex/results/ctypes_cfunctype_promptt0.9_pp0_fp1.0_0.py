import ctypes
# Test ctypes.CFUNCTYPE
test_functype.test_one_arg.restype = ctypes.CFUNCTYPE(c_char_p)
x = test_functype.test_one_arg(b"hello")
assert x(b"spam") == b"hello, spam"
assert type(x) is ctypes.CFUNCTYPE(c_char_p)

# XXX(nnorwitz): my compiler(mingw) fails with the following error:
##error: expected ',' or ';' before '__asm__'
##error: expected declaration specifiers or '...' before '(' token
##error: initializer element is not constant
xs = test_functype.test_one_arg(b"hello")
assert xs(b"spam") == b"hello, spam"

test_functype.test_defaults_1.restype = ctypes.CFUNCTYPE(c_int, c_int, c_int)
f = test_functype.test_defaults_1()

print(f(1, 2))
print
