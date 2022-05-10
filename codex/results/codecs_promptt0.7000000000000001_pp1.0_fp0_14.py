import codecs
# Test codecs.register_error:

def look(what):
    print "Registry: "
    for name, obj in codecs.__dict__.items():
        if isinstance(obj, codecs.CodecInfo):
            print name, obj
    print
    print "Lookup: "
    print "  ", codecs.lookup(what)
    print
    print "Getencoder/getdecoder: "
    print "  ", codecs.getencoder(what)
    print "  ", codecs.getdecoder(what)
    print
    print "Getreader/getwriter: "
    print "  ", codecs.getreader(what)
    print "  ", codecs.getwriter(what)
    print

look('latin_1')
look('iso-8859-1')
look('iso-8859-15')
look('iso-8859-9')
look('iso-8859-10')
look('iso-8859-11')
look('iso-8859-13')
look('iso-8859-14')
look('iso-8859
