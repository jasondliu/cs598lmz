import codecs
# Test codecs.register_error


errmods = map(__import__, ['encodings.undefined', 'encodings.backslashreplace',
    'encodings.replace', 'encodings.xmlcharrefreplace',
    'encodings.nameprep', 'encodings.punycode'])

