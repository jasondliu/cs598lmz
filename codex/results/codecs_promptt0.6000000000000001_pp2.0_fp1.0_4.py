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
r = codecs.getreader("gbk")(sys.stdin)
print("Type some gbk encoded text:")
print(r.read())

# Test codecs.getwriter
w = codecs.getwriter("gbk")(sys.stdout)
print("Type some text:")
w.write(sys.stdin.read())
