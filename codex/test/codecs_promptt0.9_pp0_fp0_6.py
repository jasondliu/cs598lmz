import codecs
# Test codecs.register_error
def bad_errorhandler(exception):
    return (u'\ufffe', exception.end)
codecs.register_error('test', bad_errorhandler)
a = 'abc\xff'
#       1234567
enc = codecs.getencoder('utf-16be')
dec = codecs.getdecoder('utf-16be')
# check that we don't get a recursion error (issue #25796)
test = codecs.getdecoder('utf-16be')(enc(a)[0])[0]
