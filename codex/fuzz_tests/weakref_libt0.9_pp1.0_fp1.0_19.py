import weakref

import epyunit.debug.checkRDbg


x = object()
@epyunit.debug.checkRDbg.addObserver
def obsfn(arg=None):
    print "obsfn:",arg

# call
weakref.ref(x)
obsfn()

print "DONE"
