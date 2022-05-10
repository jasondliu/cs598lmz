import codecs
# Test codecs.register_error()

def test_register_error():
    # Test codecs.register_error()
    import codecs
    def bad_handler(exception):
        raise TypeError("bad handler")
    def bad_handler2(exception):
        raise TypeError("bad handler")
    def good_handler(exception):
        return (u"\ufffd", exception.end)
    def good_handler2(exception):
        return (u"\ufffd", exception.end)
    def good_handler3(exception):
        return (u"\ufffd", exception.end)
    def good_handler4(exception):
        return (u"\ufffd", exception.end)
    def good_handler5(exception):
        return (u"\ufffd", exception.end)
    def good_handler6(exception):
        return (u"\ufffd", exception.end)
    def good_handler7(exception):
        return (u"\ufffd", exception.end)
    def good_handler8(exception):
        return (u
