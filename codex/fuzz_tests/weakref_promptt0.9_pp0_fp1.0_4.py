import weakref
# Test weakref.ref on the sequence object.

class X(list):
    pass

def cb(obj):
    print "X's __del__ was called!"

w = weakref.ref(X(), cb)
print w() is None # False
del X
print w() is None # True
w() is None
   
    
    

 

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyrig
