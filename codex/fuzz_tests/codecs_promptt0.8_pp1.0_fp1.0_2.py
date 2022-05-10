import codecs
# Test codecs.register_error("ignore")
codecs.register_error("ignore", lambda err: (u"\ufffd", err.start + 1))

print '#', repr(u"abcd\uac00".encode("euc-kr", "ignore"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "replace"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "xmlcharrefreplace"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "backslashreplace"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "namereplace"))

print '#', repr(u"abcd\uac00".encode("euc-kr", "ignore"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "replace"))
print '#', repr(u"abcd\uac00".encode("euc-kr", "xmlchar
