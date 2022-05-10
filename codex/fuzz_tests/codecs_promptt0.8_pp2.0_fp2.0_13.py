import codecs
# Test codecs.register_error

fp = open(TESTFN, mode='w')
fp.write('\xff')
fp.close()

fp = open(TESTFN, mode='r', encoding='ascii')
try:
    fp.read()
except UnicodeDecodeError as e:
    pass
else:
    raise Exception("should have gotten a decode error")
fp.close()

def noconvert(exc):
    return (str(exc.object[exc.start:exc.end]), exc.end)
codecs.register_error('test.noconvert', noconvert)

fp = open(TESTFN, mode='r', encoding='ascii', errors='test.noconvert')
result = fp.read()

if result != '\xff':
    raise Exception("bad result")
fp.close()

# Test surrogateescape codec

f = io.StringIO()
try:
    f.write(bytes([251]))
except ValueError:
    pass

f = io.StringIO()
f.write(bytes([251]))

