import codecs
# Test codecs.register_error("strict")

# This test is from http://bugs.python.org/issue1773263
#
# The codec bug is that an unconditioned "return" is in the wrong place
# in the surrogatepass_errors() routine, which is used by register_error("strict").
# When used with an encoding that swallows surrogates such as "utf-16",
# the problem results in an infinite loop.

import codecs
import sys

class Utf16Escape(object):
    def encode(self, input, errors='strict'):
        i = 0
        output = []
        while i < len(input):
            if input[i] == '\\':
                output.append(input[i+1:i+3].decode('hex'))
                i += 3
            else:
                output.append(input[i])
                i += 1
        return (''.join(output), len(input))
    def decode(self, input, errors='strict'):
        i = 0
        output = []
