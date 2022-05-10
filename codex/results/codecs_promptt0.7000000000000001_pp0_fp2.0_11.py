import codecs
# Test codecs.register_error() with non-empty error_handler_type

import encodings

class LookupError1(Exception):
    pass

class LookupError2(Exception):
    pass

class LookupError3(Exception):
    pass

class LookupError4(Exception):
    pass

def handler1(ex):
    raise LookupError1(ex.args[0])

def handler2(ex):
    raise LookupError2(ex.args[0])

def handler3(ex):
    raise LookupError3(ex.args[0])

def handler4(ex):
    raise LookupError4(ex.args[0])

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors,
                                     {'A': u'\u20ac'})
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors,
                                     {128: u'
