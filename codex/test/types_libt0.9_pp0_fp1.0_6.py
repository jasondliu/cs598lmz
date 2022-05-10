import types
types.__dict__.setdefault('MemberDescriptorType', types.MemberDescriptorType)
types.__dict__.setdefault('GetSetDescriptorType', types.GetSetDescriptorType)


# Add missing __next__ to OrderedDict
if hasattr(collections, 'OrderedDict'):
    try:
        collections.OrderedDict.__iter__
        collections.OrderedDict.__next__
    except (AttributeError, ):
        # Python < 3
        # from clu.naming import nameof
        from collections import deque
        from itertools  import islice as iterslice
        from functools  import wraps as fwraps
        
        def empty(self, *args, **kwargs):
            return getattr(deque(), self.__name__)(*args, **kwargs)
