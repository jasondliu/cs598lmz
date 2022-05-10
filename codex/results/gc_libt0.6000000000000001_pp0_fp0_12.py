import gc, weakref

class Object(object):
    def __init__(self):
        self.name = "object"
    def __repr__(self):
        return self.name

class Invoker(Object):
    def __init__(self, obj):
        self.name = "invoker"
        self.obj = obj
        def callback(wr, selfref=weakref.ref(self)):
            print "callback"
            self = selfref()
            print "callback: self =", self
            if self is not None:
                self.callback_done = True
        self.callback_done = False
        weakref.ref(obj, callback)

def main():
    obj = Object()
    inv = Invoker(obj)
    print "inv.obj =", inv.obj
    print "inv.callback_done =", inv.callback_done
    del obj
    gc.collect()
    print "inv.callback_done =", inv.callback_done

if __name__ == "__main__":
    main()
