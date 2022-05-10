import codecs
# Test codecs.register_error()
def custom_handler(exception):
    return u"%" + str(ord(exception.object[exception.start]))
codecs.register_error("custom_handler", custom_handler)
s = u"\u1234"
