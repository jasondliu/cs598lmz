import codecs
# Test codecs.register_error

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        # This is the error we are looking for
        return (u"\ufffd", exc.end)
    # Call the default handler for all other errors
    return codecs.xmlcharrefreplace_errors(exc)

codecs.register_error("test.replace_error", replace_error)

# The codecs module uses "test.replace_error" to look up the error handler
# function
