import codecs
# Test codecs.register_error  and codecs.lookup_error


def search_function(encoding):
    if encoding == "test.name":
        return codecs.lookup_error("replace")
    elif encoding == "test.register":
        return None

codecs.register(search_function)

encoding = None

try:
    encoding = codecs.lookup_error("test.name").name
except LookupError as e:
    print(e)

try:
    encoding = codecs.lookup_error("test.register").name
except LookupError as e:
    print(e)

class LookupName:
    pass

