import weakref
# Test weakref.ref
from ns1 import A
import ns2
import ns2

def check(ob):
    try:
        hash(ob)
    except Exception as msg:
        print('hash(%r): %s' % (ob, msg))
    else:
        print('hash(%r) OK' % (ob,))
    try:
        cmp(ob, ob)
    except Exception as msg:
        print('cmp(%r, %r): %s' % (ob, ob, msg))
    else:
        print('cmp(%r, %r) OK' % (ob, ob))

for x in [None,
 1,
 2**31-1,
 2**31,
 2**63-1,
 2**63]:
    check(x)

for x in [(),
 (1,),
 (1, 2),
 (1, 2, 3),
 (1, 2, 3, 4),
 (1, 2, 3, 4, 5)]:
    check(x)

for x in [(),
 (1.0,),
 (
