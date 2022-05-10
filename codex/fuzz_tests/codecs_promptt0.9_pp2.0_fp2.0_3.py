import codecs
# Test codecs.register_error
print(pdf_decoder('\xfe\xff\xff\xff\xff\xff\xff\xff','replace'))
# Register a replacement error handler with the codecs module.
def custom_error(exception):
    print("Error:", exception)
    return("BBBBBBBB",exception.end)
codecs.register_error('custom_replace',custom_error)
print(pdf_decoder("X",'custom_replace'))
# How the codecs module deals with Unicode errors.
print("e".encode("ascii").decode("utf-8",'ignore'))
