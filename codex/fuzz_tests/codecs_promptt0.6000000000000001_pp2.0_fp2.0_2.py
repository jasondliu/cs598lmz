import codecs
# Test codecs.register_error
def my_handler(exception):
    print "my_handler called"
    return (u"my string", exception.end)
codecs.register_error("my.error", my_handler)

# Test codecs.lookup_error
codecs.lookup_error("my.error")

class MyError(Exception):
    pass

# Test codecs.lookup_error
codecs.lookup_error(MyError)

# Test codecs.getencoder
codecs.getencoder("latin-1")

# Test codecs.getdecoder
codecs.getdecoder("latin-1")

# Test codecs.getincrementalencoder
codecs.getincrementalencoder("latin-1")

# Test codecs.getincrementaldecoder
codecs.getincrementaldecoder("latin-1")

# Test codecs.getreader
codecs.getreader("latin-1")

# Test codecs.getwriter
codecs.getwriter("latin
