import gc, weakref
from pprint import pprint
gc.set_debug(gc.DEBUG_SAVEALL)
vars = []
for x in [object(),object(),object(),object()]:
    ref = weakref.ref(x)
    ref_id = id(ref)
    print 'removing %#x from gc.garbage' % ref_id
    del gc.garbage[gc.garbage.index(ref)]
    print 'appending item %#x to vars' % ref_id
    vars.append(ref)
    print 'len(gc.get_objects()) =', len(gc.get_objects())
print 'vars=',pprint(vars, width=70)
