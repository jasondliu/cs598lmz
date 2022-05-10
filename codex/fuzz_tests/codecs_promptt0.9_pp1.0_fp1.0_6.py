import codecs
# Test codecs.register_error('strict', strict_error) before executing the
# actual test.  For the tests to pass, registering this error handler must
# not raise an exception!
try:
    codecs.register_error('strict', strict_error)
except LookupError:
    raise unittest.SkipTest("detected problem when registering 'strict' "
        "error handler")

# register(decoding_error) expects two arguments

def s_decoder(input, errors):
    return "something", len(input)

def s_encoder(input, errors):
    return "something else", len(input)

class test_iterators(unittest.TestCase):
    def test_wrongargs(self):
        # too few arguments
        try:
            codecs.register()
        except TypeError:
            pass
        else:
            self.fail()
        # function required
        try:
            codecs.register(1)
        except TypeError:
            pass
        else:
            self.fail()
        # argument must be callable
        # this is
