import weakref

from . import _internal


class _Object(object):
    @classmethod
    def _clsinit(cls):
        cls.__name__ = cls.__name__.replace('_', '')

    @classmethod
    def _dynamic_attrs(cls):
        return dict(
            (k, v) for k, v in cls.__dict__.items() if not k.startswith('_'))

    def __init__(self, id, **kwargs):
        try:
            self._obj = _internal.objects[id]
        except KeyError:
            self._obj = _internal.Object(id, **kwargs)
            self._obj.extend(self._dynamic_attrs())
            _internal.objects[id] = self._obj
        else:
            self._obj.extend(kwargs)

