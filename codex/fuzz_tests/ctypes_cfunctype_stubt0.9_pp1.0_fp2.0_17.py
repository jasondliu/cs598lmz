import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

data = list(range(10))
for i in xrange(3):
    start = datetime.now()
    objgraph.show_growth(limit=5)
    end = datetime.now()
    print (end - start).total_seconds()
    data.append((i, start, end, fun))




for i in xrange(2):
    start = datetime.now()
    objgraph.show_growth(limit=5)
    end = datetime.now()
    print (end - start).total_seconds()
    data.append((i, start, end, fun))

print objgraph.count(str)
print objgraph.count(FUNTYPE)
print objgraph.count(list)
print objgraph.count(int)
print objgraph.count(tuple)
print objgraph.count(tuple_detail)




print objgraph.count(str)
print objgraph.count(FUNTYPE)
print objgraph.count(list)
print objgraph.count(int)
print objgraph.count(tuple)
