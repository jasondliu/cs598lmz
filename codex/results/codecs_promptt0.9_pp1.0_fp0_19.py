import codecs
# Test codecs.register_error()
fp = codecs.open("\udce7\udce8\u058a", "w", encoding="iso8859_9")
fp.write("\u05d0")
fp.close()
