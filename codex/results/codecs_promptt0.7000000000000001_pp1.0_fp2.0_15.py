import codecs
# Test codecs.register_error and xml.parsers.expat.ExpatError
# on Python 2.7.2, under Windows 7 and Linux, after installing
# PyXML 0.8.4

# This file is UTF-8 encoded.

# This line should trigger an error.
x = u'\ud800'

# Output:
# Traceback (most recent call last):
#   File "xml_expat_error.py", line 9, in <module>
#     x = u'\ud800'
#   File "C:\Program Files (x86)\Python27\lib\encodings\utf_8.py", line 16,
#     in encode
#       return codecs.utf_8_encode(input, errors, True)
# UnicodeEncodeError: 'utf8' codec can't encode character u'\ud800' in
# position 0: surrogates not allowed
#
# At this point, if I continue running the code, it works perfectly.
# I get no errors, and everything works as expected.

# This part is present just to make sure that expat isn't broken
