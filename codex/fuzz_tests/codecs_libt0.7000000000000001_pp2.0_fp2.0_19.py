import codecs
codecs.open('test.txt', 'r', 'utf-8')

# unicode: how python stores strings

# u'some string'

# utf-8: how you encode unicode in bytes

# 'some string'.encode('utf-8')

# when you read text from a file, python tries to be helpful and
# decode the bytes for you using your system's default encoding.
# this is mostly fine, but can bite you when you move to a different
# system with a different default encoding.

# always encode/decode explicitly

# always open files in binary mode

# always specify the encoding when opening a text file

# always check the encoding that was used to decode

# use the codecs module to open files in different encodings


# unicode sandwich
# bytes in <-> unicode out
# bytes out <-> unicode in

# unicode in <-> unicode out
# unicode in <-> bytes out

# e.g.

# unicode in <-> unicode out
# unicode in <-> bytes out

# u'hello'.
