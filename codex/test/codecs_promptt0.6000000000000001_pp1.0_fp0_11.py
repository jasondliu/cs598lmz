import codecs
# Test codecs.register_error()

import codecs
import encodings
# import encodings.ascii

def my_error_handler(err):
    raise err

codecs.register_error("my-error-handler", my_error_handler)

# codecs.register_error("my-error-handler", lambda err: None)
# codecs.register_error("my-error-handler", lambda err: (u"X", err.end))
# codecs.register_error("my-error-handler", lambda err: (u"X", err.end))
# codecs.register_error("my-error-handler", lambda err: (u"X", err.end))
# codecs.register_error("my-error-handler", lambda err: (u"X", err.end))
# codecs.register_error("my-error-handler", lambda err: (u"X", err.end))

codecs.register_error("my-error-handler", my_error_handler)

# codecs.register_error("my-error-handler", lambda err:
