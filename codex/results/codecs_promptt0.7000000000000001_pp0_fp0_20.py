import codecs
# Test codecs.register_error
#
# This tests that a new error handling function can be registered and that
# it can be used to override the default handling of a UnicodeError exception
# from the decoding process.
#
# There is no specification of the behaviour of codec error handling
# functions, so this test is simply for completeness and to document the
# current behaviour.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
# Modified by Martin v. Loewis.
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTREPLACE ALL.

import codecs

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs
