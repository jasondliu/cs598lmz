import gc, weakref

def f():
    s = 'I live!'
    print s
    return s

def demo(cache):
    print 'Setting up cache'
    for i in xrange(10):
        cache[str(i)] = f()
    print '\nCleaning up:'
    del cache
    print 'Should live:', f()
    gc.collect()
    print 'Should be dead:', f()


cache = weakref.WeakValueDictionary()
demo(cache)
</code>
The output of this code is
<code>Setting up cache
I live!
I live!
I live!
I live!
I live!
I live!
I live!
I live!
I live!
I live!

Cleaning up:
Should live: I live!
Should be dead: I live!
</code>
I'm trying to understand why the string still lives after the <code>gc.collect</code>?
Thank you.


A:

The <code>WeakValueDictionary</code> doesn't hold strong references to the keys. The <
