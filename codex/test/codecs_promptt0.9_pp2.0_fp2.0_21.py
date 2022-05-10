import codecs
# Test codecs.register_error
body_encoding_error_handler = lambda exc: (u'\ufffd' + codecs.BOM_UTF8.decode("utf-8"), exc.end)
codecs.register_error("test.body_encoding_error_handler", body_encoding_error_handler)
