import codecs
# Test codecs.register_error

def lookup(name):
    if name == "test":
        return lambda x: u"\u1234"

codecs.register_error("test", lookup)

