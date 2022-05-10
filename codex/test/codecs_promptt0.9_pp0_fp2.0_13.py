import codecs
# Test codecs.register_error

def lookup(err):
    print("lookup(", err, ")")
    if err == "test":
        return codecs.lookup_error("replace")
