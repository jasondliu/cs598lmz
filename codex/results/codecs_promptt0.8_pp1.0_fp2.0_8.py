import codecs
# Test codecs.register_error
def new_encoder(err):
    return 'ZZX'
codecs.register_error('test.notanencoder', new_encoder)
s = 'abc'
try:
    codecs.encode(s, 'test.notanencoder')
except TypeError:
    pass
else:
    print('Failed to raise TypeError with new_encoder')
# Test codecs.register_error
def new_decoder(err):
    return 'ZZX', 1
codecs.register_error('test.notadecoder', new_decoder)
s = 'abc'
try:
    codecs.decode(s, 'test.notadecoder')
except TypeError:
    pass
else:
    print('Failed to raise TypeError with new_decoder')
# Test codecs.register_error
def new_error_handler(err):
    return 'ZZX'
codecs.register_error('test.notanerrorhandler', new_error_handler)
s = 'abc'
try:
    codecs.en
