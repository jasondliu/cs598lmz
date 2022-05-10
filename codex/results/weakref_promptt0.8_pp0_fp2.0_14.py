import weakref
# Test weakref.reference(obj, callback)

class Callback:
    # This remembers the callback for the instances of this class
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self.callback = None
        return self

    def set(self, callback):
        # This remembers the callback
        assert self.callback is None, 'callback already set'
        assert callable(callback), 'callback is not callable'
        self.callback = callback

    def __del__(self):
        # When an instance of this class is garbage collected, this calls the
        # callback with the dead instance as argument
        assert self.callback is not None, 'callback not set'
        self.callback(self)

def callback(ob):
    # This prints a message when a target is collected
    print('collected', ob)

def create_obj():
    # This creates a new target
    target = Callback()
    # This creates a weak reference to the target and binds the callback to
    # the reference
   
