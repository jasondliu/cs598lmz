import weakref
# Test weakref.ref() on a user-defined class with a __del__ method.
class C:

    def __del__(self):
        pass


class D:

    def __del__(self):
        pass


class E(D):
    pass


class G:

    def __del__(self):
        pass


class H(G):

    def __del__(self):
        pass


class I(H):
    pass


class J(H):

    def __del__(self):
        pass


class K(J):
    pass


class L(J):
    pass
# Create some instances.
c = C()
d = D()
e = E()
g = G()
h = H()
i = I()
j = J()
k = K()
l = L()
# Create some weak references to the instances.
c_ref = weakref.ref(c)
d_ref = weakref.ref(d)
e_ref = weakref.ref(e)
g_ref = weakref.ref(g)
h_ref
