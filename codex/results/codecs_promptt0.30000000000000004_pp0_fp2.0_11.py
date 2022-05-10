import codecs
# Test codecs.register_error

import codecs
import sys

def fail(msg):
    print(msg)
    sys.exit(1)

def test(name, encoder, decoder, input, expected):
    print('Test:', name)
    print('input:', input)
    print('expected:', expected)
    print('encoded:', encoder(input)[0])
    print('decoded:', decoder(encoder(input)[0])[0])
    if decoder(encoder(input)[0])[0] != expected:
        fail('decoded value not as expected')

def test_error(name, encoder, decoder, input, expected):
    print('Test:', name)
    print('input:', input)
    print('expected:', expected)
    try:
        print('encoded:', encoder(input)[0])
    except UnicodeEncodeError as e:
        print('exception:', e)
        if str(e) != expected:
            fail('exception not as expected')
    else:
        fail('missing exception')
