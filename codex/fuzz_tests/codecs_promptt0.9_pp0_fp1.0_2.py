import codecs
# Test codecs.register_error()
#

import codecs
import sys

class CodecTest:
    codec = None
    #
    # Test encoder
    #
    def testIncrementalEncoder(self, input, errorhandler):
        #
        # This test assumes that the character 'a' will be encoded to
        # the byte 'a'
        #
        if self.codec is None:
            raise RuntimeError, "could not import codec " + self.codec

        encoder = codecs.getincrementalencoder(self.codec)()
        encoder.set_error_handler(errorhandler)

        for ch in input:
            for byte in encoder.encode(ch):
                assert byte == ch, (
                    "Unexpected byte returned by encoder: " + repr(byte)
                    )

            for byte in encoder.encode(u"", True):
                assert byte == ch, (
                    "Unexpected byte returned by encoder: " + repr(byte)
                    )
        #
        # We don't test finalizing the encoder as we don't (yet)
