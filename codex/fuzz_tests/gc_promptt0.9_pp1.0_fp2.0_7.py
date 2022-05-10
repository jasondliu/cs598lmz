import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by forcing collectable objects to be freed.

    # Do it twice to ensure gc.collect() is a nop when there is no work to do

al= []
bl= []
cl= []
dl= []
el= []
fl= []
gl= []
hl= []
il= []
ll=[al,bl,cl,dl,el,fl,gl,hl,il]
zl = weakref.WeakValueDictionary()

# In previous versions large objects were deallocated by this script
# using delattr(locals(), 'big_zeros') followed by gc.collect().
# delattr() didn't seem reliable so the list.remove() hack works.
big_zeros = []
for i in range(100):
    big_zeros.insert(0, [0,0,0,0,0,0,0,0,0,0])

def make_uncollectable():
    # Create a cycle with a dict in a finalizer and an instance in a list.
    # This cycle should be detected and broken by collect(). The
    # finalizer shouldn't
