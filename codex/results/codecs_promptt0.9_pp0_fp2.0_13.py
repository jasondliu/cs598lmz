import codecs
# Test codecs.register_error

def lookup(err):
    print("lookup(", err, ")")
    if err == "test":
        return codecs.lookup_error("replace")
raise Error("test")

codecs.register_error("test", lookup)
codecs.lookup_error("test")(Error("test"))
