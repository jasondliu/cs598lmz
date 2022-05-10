import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return 1.0

from multiprocessing.managers import DictProxy, BaseProxy
s = BaseProxy(DictProxy).__getstate__(DictProxy)
v = s['_cache']['_id']
s = Client(authkey=v, serializer='pickle')
s.connect(address)
s.send(fun)
s.recv_bytes()
s.send(fun)

print('done')
</code>
Updated my answer with more information.

