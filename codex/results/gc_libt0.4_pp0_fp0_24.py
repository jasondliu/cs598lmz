import gc, weakref
from gc import get_referents
from weakref import WeakKeyDictionary
from weakref import WeakValueDictionary
from weakref import ref
from weakref import proxy
from weakref import CallableProxyType
from weakref import ProxyType
from weakref import getweakrefcount
from weakref import getweakrefs
from weakref import WeakSet
from weakref import ReferenceType
from weakref import finalize

from test import support

class T(object):
    pass

class C(object):
    pass

class D(C):
    pass

class E(C):
    pass

class F(D, E):
    pass

class G(object):
    pass

class H(G):
    pass

class I(H):
    pass

class J(I):
    pass

class K(J):
    pass

class L(K):
    pass

class M(L):
    pass

class N(M):
    pass

class O(N):
    pass

class P(O):
    pass


