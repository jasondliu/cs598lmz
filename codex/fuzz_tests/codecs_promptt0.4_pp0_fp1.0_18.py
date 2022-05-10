import codecs
# Test codecs.register_error
def my_ignore_error(exception):
    print("Ignoring", exception)
    return (u'', exception.end)
codecs.register_error("ignore", my_ignore_error)
print(codecs.decode("abc\x80\x81\x82\x83", "ascii", "ignore"))

# Test codecs.register_error
def my_replace_error(exception):
    print("Replacing", exception)
    return (u'\ufffd', exception.end)
codecs.register_error("replace", my_replace_error)
print(codecs.decode("abc\x80\x81\x82\x83", "ascii", "replace"))

# Test codecs.register_error
def my_xmlcharrefreplace_error(exception):
    print("XML char ref replacing", exception)
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)
codecs.register_error("xmlcharrefreplace", my_xml
