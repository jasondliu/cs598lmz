import codecs
# Test codecs.register_error for value errors.



# Change the behaviour of a registered error handler.  See issue #17270
import email
import codecs
def handle_special(exc):
    return (b"ignored", exc.end)
codecs.register_error("ignore", handle_special)
