import codecs
# Test codecs.register_error to handle poorly encoded input
# Specifically, \xa1 (hex), which is \xc3\xa1 in utf-8,
# is not a valid ascii symbol
text = codecs.open("test.txt", encoding='latin-1', errors='strict').read()

# "test" is "t\xe9st" when latin-1 encoded
