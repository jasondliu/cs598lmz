import _struct
# Test _struct.Struct on the returned type format.
tp_fmt = _struct.Struct('@P').format

for i in xrange(gcp):
    refcnt = sys.getrefcount(arr)
    c[i] = 1
    arr[i] = None
    c[i] = 0
    newrefcnt = sys.getrefcount(arr)
