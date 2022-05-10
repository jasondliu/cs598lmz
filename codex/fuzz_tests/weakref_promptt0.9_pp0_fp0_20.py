import weakref
# Test weakref.ref.__init__ creation of a same-argument bound method

# This Case works

class A:
    def f1(me):
        pass

    def f2(me):
        pass

class B:
    def f(me):
        pass

# self > instance, unbound > bound
for f in A().f1, A().f2, B.f:
    try:
        weakref.ref(f)
    except TypeError:
        print("TypeError raised")



# This case fails: 
# when 'B.f' is replaced with 'A().f1' or 'A().f2', it works. Why?

# TypeError: cannot create weak reference to bound method without ref to class
# in A().f1, A().f2, B.f:
# reference is weak because A and B are immediate, but not in instance?

class A:
    def f1(me):
        pass

    def f2(me):
        pass

class B:
    def f(me):
        pass

a_ref, f1
