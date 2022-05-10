import codecs
# Test codecs.register_error
for name in "replace", "ignore", "xmlcharrefreplace":
    codecs.register_error(name, codecs.strict_errors)

# Test codecs.lookup_error
for name in "replace", "ignore", "xmlcharrefreplace":
    codecs.lookup_error(name)

# Test codecs.lookup_error with unknown name
try:
    codecs.lookup_error("foo")
except LookupError:
    pass

# Test codecs.lookup_error with empty name
try:
    codecs.lookup_error("")
except LookupError:
    pass

# Test codecs.lookup_error with None name
