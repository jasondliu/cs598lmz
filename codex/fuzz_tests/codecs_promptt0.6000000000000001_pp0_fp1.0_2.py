import codecs
# Test codecs.register_error
# See http://bugs.python.org/issue4524
def test_register_error():
    import sys
    import codecs
    import encodings.idna
    assert encodings.idna.nameprep is not None
    def my_exc(exc):
        return (u"", exc.end)
    codecs.register_error("test.idna", my_exc)
    from encodings import idna
    enc = idna.getregentry()
    assert enc is not None
    assert enc[2](u"\u1234") == (u"", 1)
    #
    # A "strict" error handler must raise a UnicodeEncodeError
    def my_exc(exc):
        return (u"", exc.end)
    codecs.register_error("test.idna", my_exc, True)
    from encodings import idna
    enc = idna.getregentry()
    assert enc is not None
    raises(UnicodeEncodeError, enc[2], u"\u1234")
    #
   
