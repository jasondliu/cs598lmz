import weakref
# Test weakref.ref() on an instance of the built-in type dict()
functor = dict(a="foo", b="bar")
func_ref = weakref.ref(functor)
print(func_ref)
print(func_ref())
print(func_ref() is functor)
del functor

class doppelDict2(dict):
    '''
    Example of a reference-counted object
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ref_count = 1  # start with a ref count to 1

    def __str__(self):
        return ('<doppelDict2 object referenced to '
                f'{self.ref_count} objects>')

    def __del__(self):
        print(f'Object deleted with ref count: {self.ref_count}')

    def __new__(cls, *args, **kwargs):
        obj = dict.__new__(cls, *args, **kwargs)
        # Add object to the
