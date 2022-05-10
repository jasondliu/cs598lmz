import bz2
# Test BZ2Decompressor
assert_equal(BZ2Decompressor().decompress(b"BZh91AY&SY" b"\0"*25), b"Hello")
# Test BZ2File
f = bz2.BZ2File(BytesIO(b"BZh91AY&SY" b"\x00"*25))
lines = f.readlines()
assert_equal(b"".join(lines), b"Hello")
f.close()

# Test that we can enable compression for HTTPS connections that we wrap.
if HTTPSConnection:
    wrapped = CompressedHTTPSConnection(HOSTNAME, PORT)
    wrapped.set_debuglevel(DEBUGLEVEL)
    wrapped.request("GET", "/")
    resp = wrapped.getresponse()
    resp.read()
    wrapped.close()

# Test that we can use CompressedHTTPHandler with urllib2
if urlopener:
    opener = urllib.request.build_opener(CompressedHTTPHandler)
    f = opener.open("http://%s:%d/" % (HOSTNAME, P
