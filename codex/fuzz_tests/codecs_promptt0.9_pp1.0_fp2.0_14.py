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

codecs.lookup_error(LookupName)
ErrorClass = LookupName
codecs.lookup_error(ErrorClass)


# Test 'unknown' codec

import codecs
# Test the 'unknown' codec that allows to register the
# encoder, decoder and streamwriter.


class StreamWriterTest(codecs.StreamWriter):
    pass


class IncrementalEncoderTest(codec
