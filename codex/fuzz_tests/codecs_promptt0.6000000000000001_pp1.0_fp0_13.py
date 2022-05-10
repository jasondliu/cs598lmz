import codecs
# Test codecs.register_error, with a custom replacement error handler.
# This is an extremely complicated way to replace "a" by "b", but
# it serves as a good test of the codecs module.
import codecs, sys

class Test:

    def __init__(self, *repl):
        self.repl = repl

    def __call__(self, error):
        return (self.repl[0], error.start + 1)

def test(encoding):
    codecs.register_error(encoding, Test(*encoding[2:]))
    print(codecs.encode("a", encoding))

test("test.replace")
test("test.ignore")
test("test.xmlcharrefreplace")
test("test.backslashreplace")
test("test.namereplace")
test("test.strict")
test("test.surrogateescape")
test("test.surrogatepass")
test("test.strict")
test("test.surrogateescape")
test("test.surrogatepass")
test("test.strict")
test("test.surrogate
