import codecs
# Test codecs.register_error
try:
    codecs.register_error("Pilou", codecs.lookup("ascii"))
except Exception, e:
    print("Exception: %s" % e)
    pass
try:
    codecs.register_error("Pilou", codecs.lookup("ascii"), "replace")
except Exception, e:
    print("Exception: %s" % e)
    pass
codecs.register_error("Pilou", codecs.lookup("ascii"), "replace", 123)
codecs.register_error("Pilou2", codecs.lookup("ascii"), "replace")
codecs.register_error("Pilou3", codecs.lookup("ascii"), "replace", "XYZ")
codecs.register_error("Pilou4", codecs.lookup("ascii"), "replace", "XYZ")
codecs.register_error("Pilou5", codecs.lookup("ascii"), "replace", "XYZ")
codecs.register_error("P
