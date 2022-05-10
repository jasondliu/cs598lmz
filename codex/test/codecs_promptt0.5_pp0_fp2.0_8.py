import codecs
# Test codecs.register_error

# This test is not exhaustive.  It tests that some of the error
# handlers work, and that the backslashreplace handler is in place
# for some codecs.

import codecs
import string
import sys

# Codecs whose errors are not 'strict'
nonstrict_codecs = ['rot_13', 'string_escape', 'string_escape']

# Codecs whose errors are 'strict'
strict_codecs = ['ascii', 'base64_codec', 'bz2_codec', 'hex_codec',
                 'idna', 'mbcs', 'quopri_codec', 'raw_unicode_escape',
                 'rot_13', 'string_escape', 'uu_codec', 'zlib_codec']

# Codecs whose errors are 'replace'
