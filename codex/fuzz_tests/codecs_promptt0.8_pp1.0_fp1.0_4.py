import codecs
# Test codecs.register_error()

try:
    # This causes a syntax error which will be caught in the except clause.
    codecs.register_error("test.faulty_strict", ("foo", "bar"))
except SyntaxError:
    pass
else:
    # Make sure this doesn't raise an exception
    codecs.lookup_error("test.faulty_strict")

@contextlib.contextmanager
def recode_to_utf_8_strict(errors = "strict"):
    codecs.register_error("test.recode_strict",
                          lambda exc: (u"\ufffd", exc.end))
    yield
    del codecs.lookup_error('test.recode_strict')

@contextlib.contextmanager
def recode_to_utf_8_ignore(errors = "ignore"):
    codecs.register_error("test.recode_ignore",
                          lambda exc: (u"", exc.end))
    yield
    del codecs.lookup_error('test.recode_ignore')
