import codecs
codecs.register_error('not-enough-data', partial(ReadFmt, 'not-enough-data'))
m = re.match(b'(.)(.)(.)', b'abc')
m.groups()

# (b'a', b'b', b'c')

m = re.match(b'(.)(.)*(.)', b'abc')
m.groups()

# (b'a', b'b', b'c')

m = re.match(b'(.)(.)*?(.)', b'abc')
m.groups()

# (b'a', b'', b'c')

m = re.match(b'(.)(.*)(.)', b'abc')
m.groups()

# (b'a', b'bc', b'c')

m = re.match(b'(.)(.*?)(.)', b'abc')
m.groups()

# (b'a', b'b', b'c')

m = re.match(b'(?s)(.)(.*)(.)', b'abc
