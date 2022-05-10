import codecs
# Test codecs.register_error('test', codecs.lookup_error('replace'))
codecs.register_error('test', codecs.lookup_error('replace'))
codecs.register_error('strict', codecs.lookup_error('strict'))

"""
Cp1252 codec that encodes 0x85 as <U+2026> (horizontal ellipsis),
and encodes <U+2026> as 0x85.

Also, encodes 0x83 as <U+201c> (left double quotation mark),
and encodes <U+201c> as 0x83.

Also, encodes 0x84 as <U+201d> (right double quotation mark),
and encodes <U+201d> as 0x84.

Also, encodes 0x82 as <U+2019> (right single quotation mark),
and encodes <U+2019> as 0x82.

In addition, decode() calls unicode_internal_decode() to replace
<U+FFFD> by <U+2026>, and replace <U+2014> by <U
