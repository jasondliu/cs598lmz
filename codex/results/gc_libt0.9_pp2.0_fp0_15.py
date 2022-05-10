import gc, weakref, os

class CachedObject:
    def __init__(self, obj, filename=None):
        self.obj = obj
        self.filename = filename

def DefaultCache(createfunc, filename, lru):
    def _cache(objreturned):
        cachedref = lru.get(filename, None)
        if cachedref and cachedref() is not None:
            obj = cachedref()
            print 'Using cached file: %s'%filename
            lru[filename] = weakref.ref(obj)
            return obj
        obj = createfunc()
        lru[filename] = weakref.ref(obj)
        return obj
    return _cache

lrucache = weakref.WeakValueDictionary()
cachefunc = DefaultCache(filename='somefile', createfunc=lambda: MyBigThing, lru=lrucache)
res = cachefunc()
print res
del cachefunc, res
gc.collect()
print lrucache
</code>
This prints:
<code>Creating file: somefile
Using cached file: somefile
&lt;
