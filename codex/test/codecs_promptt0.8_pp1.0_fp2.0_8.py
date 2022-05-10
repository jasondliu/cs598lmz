import codecs
# Test codecs.register_error
def new_encoder(err):
    return 'ZZX'
codecs.register_error('test.notanencoder', new_encoder)
s = 'abc'
