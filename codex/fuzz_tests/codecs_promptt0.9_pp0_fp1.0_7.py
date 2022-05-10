import codecs
# Test codecs.register_error for UnicodeEncodeError
# BZ165562: itemgetter: UnicodeEncodeError when printing elements (characters lost)
# Note that an other fix was provided as part of BZ165562
# Cyril Bonté pointed out this second issue and a fix is proposed as
# part of this bug
import encodings


def encode(e):
    return 1


def decode(e):
    return 1


# Handle the following UnicodeEncodeError:
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xfffd' in position 4: ordinal not in range(128)
encodings.register_error("err1", encode)
encodings.register_error("err2", decode)
