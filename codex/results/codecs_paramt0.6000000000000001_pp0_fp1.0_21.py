import codecs
codecs.register_error('replace_spaces', codecs.replace_errors([0x20]))

with codecs.open('unicode_text.txt', 'r', 'utf-8', 'replace_spaces') as f:
    print(f.read())

# The default handler, 'strict', will raise an exception.

with codecs.open('unicode_text.txt', 'r', 'utf-8') as f:
    print(f.read())

# The backslashreplace handler will replace the invalid character
# with a backslash and a hexadecimal representation of the byte.

with codecs.open('unicode_text.txt', 'r', 'utf-8', 'backslashreplace') as f:
    print(f.read())
