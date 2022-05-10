import codecs
# Test codecs.register_error:

def handler1(exc):
    print('Bad char: %s' % exc)
    return exc.args[0], exc.args[1] + 1  # Add 1 to the index

def handler2(exc):
    print('Bad char: %s' % exc)
    return ('a', exc.args[1] + 1)  # Replace char with 'a'

codecs.register_error('test', handler1)

for c in ['\x00', '\xff']:
    encoder = codecs.getencoder('ascii')
