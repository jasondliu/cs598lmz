import weakref

__all__ = ['Node', 'NodeList', 'NodeManager', 'NodeManagerProxy', 'NodeObject']

_last_id = 0

class NodeObject(object):
    def __init__(self):
        self._id = None
        self._parent = None
        self._children = None

    def _get_id(self):
        if self._id is None:
            global _last_id
            _last_id += 1
            self._id = _last_id
        return self._id

    def _set_id(self, id):
        self._id = id

    id = property(_get_id, _set_id)

    def _get_parent(self):
        if self._parent is None:
            return None
        return self._parent()

    def _set_parent(self, parent):
        if parent is None:
            self._parent = None
        else:
            self._parent = weakref.ref(parent)

    parent = property(_get_parent, _set_parent)

    @property
    def is_root(
