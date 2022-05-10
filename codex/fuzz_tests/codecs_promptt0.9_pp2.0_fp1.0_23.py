import codecs
# Test codecs.register_error for all encodings if passed an unknown
# encoding characters name.

all_encodings = codecs.aliases.aliases.values()
for encoding in all_encodings:
    try:
        codecs.lookup(encoding)
    except LookupError:
        pass
    else:
        try:
            codecs.register_error('test.name', lambda x: ' ' * len(x))
        # CPython issue35795, issue36180: pyexpat in non-validating mode can not
        # determine the length of "random" replacement data.
        except ValueError as e:
            if encoding == 'gb2312':
                msg = "replacement must be a unicode string of length 1"
            elif encoding == 'gb18030':
                msg = "replacement must be a unicode string of length 1 or 2"
            else:
                msg = "replacement must be a unicode string"
            if str(e) != "can't register unit and non-unit pmaps for encoding %s" % encoding:
                raise
            if '%
