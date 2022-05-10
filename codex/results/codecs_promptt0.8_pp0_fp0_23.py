import codecs
# Test codecs.register_error
def error_handler(exception):
    return (u"", exception.end)
codecs.register_error("test.replace", error_handler)
codecs.lookup_error("test.replace")
# Test codecs.lookup_error, codecs.register_error
try:
    codecs.lookup_error("missing.error")
except LookupError as e:
    assert type(e) is LookupError
# Test codecs.open, codecs.getreader
f = codecs.getreader("ascii")(io.BytesIO(b"\xc3\xb5"))
if hasattr(f, "buffer"):
    buffer_attr = f.buffer
    assert type(buffer_attr) is io.BufferedReader
    assert buffer_attr.name is f.name
else:
    buffer_attr = f
assert buffer_attr.name is f.name
if hasattr(buffer_attr, "seekable"):
    assert buffer_attr.seekable() # BufferedReader are seekable
assert type(buffer_attr.readable()) is
