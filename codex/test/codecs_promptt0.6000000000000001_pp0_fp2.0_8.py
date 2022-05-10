import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)

import sys
if sys.platform == 'win32':
    import msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

import unittest
