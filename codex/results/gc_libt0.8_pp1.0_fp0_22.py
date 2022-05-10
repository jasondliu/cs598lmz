import gc, weakref

from .inner import isNull, InnerValue



class Ref(InnerValue.AsStr):
    __slots__ = ['_ref']
    def __init__(self, ref):
        super().__init__(ref)
        # self._ref = ref
        # self.__setattr__('_ref', ref)
    def _toStr(self):
        return str(self._ref)
    def _toRepr(self):
        return str(self._ref)
    def _toHash(self):
        return hash(self._ref)
    def _toBool(self):
        return self._ref is not None
    def __getattr__(self, attribute):
        return getattr(self._ref, attribute)
    def __setattr__(self, attribute, value):
        return setattr(self._ref, attribute, value)
    def __call__(self, args):
        return self._ref(args)
    def __dir__(self):
        return dir(self._ref)
    def __repr__(self):
       
