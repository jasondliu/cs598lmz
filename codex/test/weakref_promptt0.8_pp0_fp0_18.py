import weakref
# Test weakref.ref()
import random

class C:
    pass

o = C()
r = weakref.ref(o)

# Accessing o directly is OK
