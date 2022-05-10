import codecs
# Test codecs.register_error
output = codecs.getwriter('ascii')(outputbuf)

def test(y):
    print((globals().keys()))
    print(3)

print((globals().keys()))
print(1)
test(2)
print(2)
output.close()

sys.stdout = stdout
