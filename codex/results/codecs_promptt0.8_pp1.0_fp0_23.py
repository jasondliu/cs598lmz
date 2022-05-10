import codecs
# Test codecs.register_error()
# Register a handler that replaces data by "!"
def replace_handler(exc):
    return (u'!', exc.start + 1)
codecs.register_error('replace', replace_handler)
print("abcabcabcabc".decode("unknown", "replace"))
# Codec specific error handling with "lookup"
def ignore_handler(exc):
    # don't do anything!
    pass
try:
    codecs.lookup_error("ignore")
except LookupError:
    # If there's no ignore handler, add one.
    codecs.register_error("ignore", ignore_handler)
print("abc".decode("utf8", "ignore"))
print("abc".decode("ascii", "ignore"))
