import codecs
# Test codecs.register_error
def gbk_decode(input, errors="strict"):
    return codecs.charmap_decode(input,errors,"gbk")
codecs.register(gbk_decode)

# Test codecs.lookup
if codecs.lookup("gbk"):
    print("gbk codec found")
else:
    print("gbk codec not found")

# Test codecs.getreader
