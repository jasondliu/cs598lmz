import codecs
# Test codecs.register_error()

def handler(exception):
    print('Error: %s' % exception)
    return '', exception.start + 1

text = 'pi: \u03c0'

decoding_error = 'strict'
print('DECODING ERROR:', decoding_error)
decoder = codecs.getincrementaldecoder('utf-8')(decoding_error)
print('  raw:', end=' ')
print(text)
print('  dec:', end=' ')
