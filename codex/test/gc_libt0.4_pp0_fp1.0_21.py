import gc, weakref

#==============================================================================
# 
#==============================================================================
class _Object(object):
    """
    Base class for all objects.
    """
    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._name = kwargs.get('name', None)
        self._parent = kwargs.get('parent', None)
        self._children = kwargs.get('children', [])
        self._data = kwargs.get('data', {})
        self._tags = kwargs.get('tags', [])
        self._references = kwargs.get('references', [])
        self._referenced_by = kwargs.get('referenced_by', [])
        self._referenced_by_weak = kwargs.get('referenced_by_weak', [])
        self._referenced_by_weak_ref = kwargs.get('referenced_by_weak_ref', [])
        self._referenced_by
