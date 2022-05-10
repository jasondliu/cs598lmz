import codecs
codecs.open('/path/to/some/file', 'r', encoding='utf-8')
# use `codecs.open` when you have to deal with non-ascii file
# in general, use `open(file, 'r')`

# if you really want to encode to ascii
u"Hello world".encode('ascii')
# or
u"Hello world".encode('ascii', 'ignore')
u"Hello world".encode('ascii', 'replace')
u"Hello world".encode('ascii', 'xmlcharrefreplace')
u"Hello world".encode('ascii', 'backslashreplace')

# convert from unicode to string
str(u"Hello world")
# convert from string to unicode
unicode(u"Hello world")

################################################################################
# Python3 does not have `unicode` or `str` type, it only has `str` type
# which is unicode string
################################################################################

# Python3
"Hello world".encode('ascii')
"Hello world".encode
