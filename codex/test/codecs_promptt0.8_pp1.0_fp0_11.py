import codecs
# Test codecs.register_error
def register_error(encoding):
    #print("register_error in %s" % encoding)
    enc = codecs.lookup(encoding)
    def func(errors='strict'):
        #print("register_error func called")
        return codecs.charmap_encode, enc.decode, None
    if func in enc.incrementalencoder:
        return
    enc.incrementalencoder.insert(0, func)
    enc.incrementalencoder.insert(0, func)
    enc.incrementalencoder.insert(0, func)
    enc.decode.__func__.incrementalencoder = enc.incrementalencoder
    enc.decode.__func__.incrementaldecoder = enc.incrementaldecoder
    enc.streamwriter.insert(0, func)
    enc.streamreader.insert(0, func)

# Test codecs.charmap_decode
