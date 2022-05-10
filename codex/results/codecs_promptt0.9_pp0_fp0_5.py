import codecs
# Test codecs.register_error
enc = codecs.getencoder("euc-jp")
dec = codecs.getdecoder("euc-jp")
s = enc("汉字", "strict")[0]
s = s[:-1] + b"\xc1\x80"
dec(s, "ignore")[0]
test_support.reap_children()
test_main()
