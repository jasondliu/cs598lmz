import codecs
# Test codecs.register_error()
import _testcapi

# The following codecs are known to be broken:
# 'charbuffer'
# XXX: the following codecs should be checked:
# 'iso2022_jp'
# 'palmos'
# 'rot_13', 'string_escape', 'uu_codec', 'zlib_codec'

# XXX: add coverage for encodings that don't have a builtin python module

# 'base64_codec', 'base64_codec'
# 'bz2_codec', 'bz2_codec'
# 'hex_codec', 'hex_codec'
# 'idna', 'idna'
# 'mbcs', 'mbcs' 'utf_8', 'utf_8'
# 'uu_codec', 'uu_codec'
# 'zlib_codec', 'zlib_codec'

def _test_encoding(encoding):
    if encoding == 'idna': raise NotImplementedError  # XXX
    if encoding == 'palmos': raise NotImplementedError  # XXX
