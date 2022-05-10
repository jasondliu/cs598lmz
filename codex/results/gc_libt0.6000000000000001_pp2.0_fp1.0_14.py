import gc, weakref, sys

class Foo(object):
    pass

def bar():
    pass

def main():
    f = Foo()
    #print "f:", f
    
    wf = weakref.ref(f)
    #print "wf:", wf
    
    b = bar
    wb = weakref.ref(b)
    #print "wb:", wb
    
    #print "wb() == b:", wb() == b
    #print "wf() == f:", wf() == f
    #print
    
    del f
    del b
    
    #print "wf():", wf()
    #print "wb():", wb()
    #print
    
    gc.collect()
    
    #print "wf():", wf()
    #print "wb():", wb()
    #print
    
    #print "wf():", wf()
    #print "wb():", wb()
    #print
    
    #print "wf():", wf()
   
