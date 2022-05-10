import codecs
# Test codecs.register_error
a="abc"
b=u"def"
c=codecs.charmap_encode(a,None,{},encoding="koi_8r")
d=codecs.charmap_decode(c[0],None,{},encoding="koi_8r")
if(d[0] != a):
    raise RuntimeError,"String was changed"
if(c[1] != 3):
    raise RuntimeError,"Short byte count"
if(d[1] != 3):
    raise RuntimeError,"Short byte count"
if(c[2] != (6,1)):
    raise RuntimeError,"Short byte count"
if(d[2] != (6,1)):
    raise RuntimeError,"Short byte count"

def c(message):
    print message
#codecs.register_error("test_decode_c",c)
#codecs.register_error("test_decode_u",c)
a=u"abc\xFF\x45\xFF\x34\xFF"
b=a
