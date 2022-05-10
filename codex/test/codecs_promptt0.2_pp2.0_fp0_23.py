import codecs
# Test codecs.register_error

def test_register_error():
    def handler(exception):
        return (u'', exception.end)

    codecs.register_error('test.ignore', handler)
    codecs.register_error('test.replace', handler)
    codecs.register_error('test.xmlcharrefreplace', handler)
    codecs.register_error('test.backslashreplace', handler)
    codecs.register_error('test.namereplace', handler)
    codecs.register_error('test.strict', handler)
    codecs.register_error('test.surrogateescape', handler)
    codecs.register_error('test.surrogatepass', handler)

def test_main():
    test_register_error()

if __name__ == "__main__":
    test_main()
