gi = (i for i in ())
# Test gi.gi_code.co_name

def f():
    for i in ():
        pass

gi = f.gi_frame.f_lasti

# Test gi.gi_code.co_firstlineno
class C:
    def f(self):
        pass

gi = C.f.gi_frame.f_lasti

# Test gi.gi_code.co_lnotab
class C:
    def f(self):
        pass

gi = C.f.gi_frame.f_lasti

# Test gi.gi_code.co_varnames
class C:
    def f(self, x):
        pass

gi = C.f.gi_frame.f_lasti

# Test gi.gi_code.co_argcount
class C:
    def f(self, x):
        pass

gi = C.f.gi_frame.f_lasti

# Test gi.gi_code.co_cellvars
class C:
    def f(self, x):
        def g():

