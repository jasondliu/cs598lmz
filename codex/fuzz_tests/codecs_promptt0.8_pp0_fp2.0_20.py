import codecs
# Test codecs.register_error to replace bad characters with a Python 'replacement'
# character
utf8reader = codecs.getreader('utf-8')
text = open('../data/random.txt', 'r').read()
# In this case, clearly utf-8 is not the right encoding. The bytes represent
# the cp1252 encoding, which is a superset of ISO-8859-1.
text = text.decode('utf-8')

def replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('Replacing: {}'.format(exc.object[exc.start:exc.end]))
        return (u'\ufffd', exc.end)
    else:
        raise TypeError

codecs.register_error('decode', replace)
utf8reader = codecs.getreader('utf-8')
text = open('../data/random.txt', 'r').read()
print(text.decode('utf-8'))

# We can also use a function to replace or ignore bad bytes or characters.
def ignore_error(error):
    print
