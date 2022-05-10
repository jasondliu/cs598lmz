import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)

for x in dir(codecs):
    print x


# Test getdefaultencoding for all encodings
# This test is only meaningful if the PYTHONIOENCODING environment
# variable is not set.
e = "utf-8"
del os.environ["PYTHONIOENCODING"]
ce = sys.getdefaultencoding()
if ce != "ascii":
    e = ce
if len(sys.argv) > 2 and sys.argv[2] == "-e":
    e = sys.argv[1]
e = codecs.lookup(e)

l = [99, 200, 85, 128, 255]
# Test whether the encoding uses ascii, but replaces outside ascii.

