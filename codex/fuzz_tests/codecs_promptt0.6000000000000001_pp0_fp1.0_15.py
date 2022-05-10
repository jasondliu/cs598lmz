import codecs
# Test codecs.register_error

import encodings
import encodings.idna
import encodings.punycode

# http://www.unicode.org/reports/tr36/#Table_Examples
# http://www.unicode.org/reports/tr32/#Table_Examples
# http://www.unicode.org/reports/tr46/#Examples
# http://www.unicode.org/reports/tr46/#ToUnicode

TESTS = [
    # ToASCII
    # Table 1: Characters Disallowed in Internationalized Domain Names
    (b'\x00', False),
    (b'\x01', False),
    (b'\x02', False),
    (b'\x03', False),
    (b'\x04', False),
    (b'\x05', False),
    (b'\x06', False),
    (b'\x07', False),
    (b'\x08', False),
    (b'\x09', False),
    (b'\x0a', False),
    (b'\x
