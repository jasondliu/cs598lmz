import _struct
# Test _struct.Struct on the returned type format.
tp_fmt = _struct.Struct('@P').format

for i in xrange(gcp):
    refcnt = sys.getrefcount(arr)
    c[i] = 1
    arr[i] = None
    c[i] = 0
    newrefcnt = sys.getrefcount(arr)
    if newrefcnt != refcnt:
        print "cellref:", i, "arr refcnt:",
        print "was" if newrefcnt > refcnt else "wasn't",
        print "decremented when cell cleared"

# Test combination of cell, list and dict
def count_refs(obj):
    return sys.getrefcount(obj) - 2 # account for gc_refs and function call

gc.collect()
cells = [cell(i) for i in range(gcp)]
cd = dict.fromkeys(cells)
cl = [(1, 1, i) for i in cells]
pcd = dict.fromkeys([(1, 1, i) for i in
