import codecs
# Test codecs.register_error()

import codecs,string

def search_function(encoding):
    if encoding!="test.baseencodingsubclass":return None
    def encode(input,errors="strict"):
        str=input.encode("latin-1",errors)
        return (str,"latin-1")
    def decode(input,errors="strict"):
        return input.decode("latin-1",errors)
    def incrementaldecoder(errors="strict"):
        # The incrementaldecoder never encodes an incomplete character.
        # We could use the IncrementalDecoder class, too, but this would
        # not be in the spirit of things.
        return codecs.getincrementaldecoder("latin-1")()

    def incrementaldecode(self,input,final=False):
        # The incrementaldecoder never encodes an incomplete character.
        # We could use the IncrementalDecoder class, too, but this would
        # not be in the spirit of things.
        return input.decode("latin-1",errors)
