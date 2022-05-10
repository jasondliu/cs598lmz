import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

class SetCallback(Callback):    
    func = FUNTYPE(setcb)
    
    def __init__(self,callback):
        self.callback = callback
    
    def __call__(self,num):
        libtest.test_setcallback(self.func)
        return self.callback(num)

#===============================================================================
# Testing
#===============================================================================
if __name__ == '__main__':
    
    # set a callback for a function in c
    def cb1(num):
        print 'number = %d' % num
    setcb = SetCallback(cb1)
    setcb(25)
    
    # set a callback with a class
    class Foo:
        def __init__(self,val=0):
            self.val = val
            
        def cb2(self,num):
            print 'number = %d' % num
            self.val += 1
            
    foo = Foo()
    setcb = SetCallback(foo.cb2)
   
