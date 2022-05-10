import codecs
# Test codecs.register_error('ign', codecs.ignore_errors)

# ---
"""
UnicodeError
"""
# unicode.encode('utf-8')
# unicode.encode('ascii')
# unicode.encode('iso-8859-1')

# ---
"""
SyntaxError
"""
# eval(u'print("\xc3\xa1")')

# ---
"""
TypeError
"""
# unicode.encode('iso-8859-1')

# ---
"""
ValueError
"""
# unicode('x') + unicode('x', 'iso-8859-1')
# unicode(b'x', 'utf-8')

# ---
"""
UnicodeDecodeError
"""
# b'\xc3\xa1'.decode('utf-8')
# b'\xc3\xa1'.decode('ascii')
# b'\xc3\xa1'.decode('iso-8859-1')
# b'\xc3\xa1'.decode('iso-8859-1',
