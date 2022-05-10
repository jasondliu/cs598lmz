import codecs
# Test codecs.register_error

# Note that we need to fake out the encodings module to make this work
import encodings
encodings.__path__ = ["dummy"]

# This is how Python sets up the default handler; we'll emulate that here
def raise_exception(exception):
    raise exception
codecs.register_error("strict", raise_exception)

# Make sure the defaults are as expected
assert codecs.lookup_error("strict") is raise_exception

# Now make sure we can override it
def ignore_exception(exception):
    return (u"", exception.end)
codecs.register_error("ignore", ignore_exception)
assert codecs.lookup_error("ignore") is ignore_exception

# Make sure the defaults are still as expected
assert codecs.lookup_error("strict") is raise_exception

# Try the replacement handler to make sure it works
codecs.register_error("strict", ignore_exception)
assert codecs.lookup_error("strict") is ignore_exception

