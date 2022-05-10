import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Add a test for the 'strict' error handler.
# The script is not loaded as UTF-8 with BOM.
# This will raise a SyntaxError with the default error handler,
# but ignore the error with 'strict'.

with open(TESTFN, "wb") as fp:
    fp.write(codecs.BOM_UTF8)
    fp.write(b'print(ascii(chr(0xdc80)))')

with open(TESTFN, "rb") as fp:
    try:
        exec(fp.read())
    except SyntaxError:
        pass
    else:
        raise TestFailed("exec did not raise SyntaxError")

with open(TESTFN, "rb") as fp:
    try:
        exec(fp.read().decode('utf-8', 'strict'))
    except SyntaxError:
        raise TestFailed("exec raised SyntaxError")

# Test for the 'ignore' error handler.
# The
