import codecs
# Test codecs.register_error
def handle_error(*args):
    print("handle_error:", args)
    return (u"\ufffd", args[1])

codecs.register_error("test.myhandler", handle_error)

# Test codecs.lookup_error
print("lookup_error:", codecs.lookup_error("test.myhandler"))

# Test codecs.strict_errors
print("strict_errors:", codecs.strict_errors)

# Test codecs.ignore_errors
print("ignore_errors:", codecs.ignore_errors)

# Test codecs.replace_errors
print("replace_errors:", codecs.replace_errors)

# Test codecs.xmlcharrefreplace_errors
print("xmlcharrefreplace_errors:", codecs.xmlcharrefreplace_errors)

# Test codecs.backslashreplace_errors
print("backslashreplace_errors:", codecs.backslashreplace_errors)

# Test codecs.namereplace_errors
