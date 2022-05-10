import codecs
# Test codecs.register_error('my_error', my_error_handler)
# codecs.register_error("my_error", my_error_handler)
# codecs.register_error("strict", strict_error_handler)
# codecs.register_error("ignore", ignore_error_handler)
# codecs.register_error("replace", replace_error_handler)
# codecs.register_error("xmlcharrefreplace", xmlcharrefreplace_error_handler)
# codecs.register_error("backslashreplace", backslashreplace_error_handler)
# codecs.register_error("namereplace", namereplace_error_handler)
# codecs.register_error("surrogateescape", surrogateescape_error_handler)
# codecs.register_error("surrogatepass", surrogatepass_error_handler)

def my_error_handler(exception):
    print("My custom error handler:", exception)
    return ("[My error handler]", 1)

def strict_error_handler(exception):
    print("Strict error handler:", exception)
    return ("[St
