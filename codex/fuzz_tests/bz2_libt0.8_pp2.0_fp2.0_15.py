import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

try:
    from cdecimal import Decimal as _cdecimal
    import cdecimal
    cdecimal_Decimal = _cdecimal
    cdecimal_getcontext = cdecimal.getcontext
except:
    cdecimal_Decimal = None
    cdecimal_getcontext = None

try:
    import cjson
    cjson_decode = cjson.decode
    cjson_encode = cjson.encode
    cjson_loads = cjson.loads
    cjson_dumps = cjson.dumps
except:
    cjson_decode = None
    cjson_encode = None
    cjson_loads = None
    cjson_dumps = None

try:
    import cPickle as _cpickle
    import cPickle
    cPickle_dumps = _cpickle.dumps
    cPickle_loads = _cpickle.loads
    cPickle_HIGHEST
