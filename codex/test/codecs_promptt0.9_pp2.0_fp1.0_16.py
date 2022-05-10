import codecs
# Test codecs.register_error; sys.setcheckinterval exceeded is
# not caught in the list of known exceptions by the way
with codecs.open("test.txt","w","iso8859-2") as outputfile:
    f = codecs.open("test.txt","r","iso8859-2")
