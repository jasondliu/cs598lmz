import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == "test.searchfunction":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

# Test that the codec is found
u = u"\u20ac"
for encoding in ("test.searchfunction", "test.searchfunction_capi"):
    assert codecs.encode(u, encoding) == codecs.encode(u, "utf-8")

# Test that the codec is not found
for encoding in ("test.searchfunction_fail", "test.searchfunction_capi_fail"):
    try:
        codecs.encode(u, encoding)
    except LookupError:
        pass
    else:
        raise AssertionError("LookupError not raised")

# Test that the codec is found, but raises an error
def search_function_error(encoding):
    if encoding == "test.searchfunction_error":
        return codecs.lookup("utf-8")
    return None
