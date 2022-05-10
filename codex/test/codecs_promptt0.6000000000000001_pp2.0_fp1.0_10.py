import codecs
# Test codecs.register_error('my_error', codecs.replace_errors)
# utf8 '\x80' -> U+FFFD
# utf8 '\xc0\x80' -> U+FFFD
# utf8 '\xc1\x80' -> U+FFFD
# utf8 '\xe0\x80\x80' -> U+FFFD
# utf8 '\xe0\x81\x80' -> U+FFFD
# utf8 '\xe0\x9f\xbf' -> U+FFFD
# utf8 '\xe1\x80\x80' -> U+FFFD
# utf8 '\xf0\x80\x80\x80' -> U+FFFD
# utf8 '\xf0\x80\x80\x81' -> U+FFFD
# utf8 '\xf0\x80\x81\x80' -> U+FFFD
# utf8 '\xf0\x81\x80\x80' -> U+FFFD
# utf8 '\xf0\x
