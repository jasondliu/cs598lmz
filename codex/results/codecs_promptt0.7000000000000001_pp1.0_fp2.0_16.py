import codecs
# Test codecs.register_error

def handler(exception):
    print('Handling {0}'.format(exception))
    return ('a', exception.start+1)

codecs.register_error('test.xmlcharrefreplace', handler)

s = '&#160;\n'

print(s.encode('ascii', 'xmlcharrefreplace'))
print(s.encode('ascii', 'test.xmlcharrefreplace'))
print(s.encode('ascii', 'test.xmlcharrefreplace').decode('ascii', 'xmlcharrefreplace'))

# Test unicode.encode()

class MyUnicode(str):
    def encode(self, encoding, errors='strict'):
        return str.encode(self, encoding, errors=errors)

s = MyUnicode('&#160;\n')

print(s.encode('ascii', 'xmlcharrefreplace'))
print(s.encode('ascii', 'test.xmlcharrefreplace'))
print(s.en
