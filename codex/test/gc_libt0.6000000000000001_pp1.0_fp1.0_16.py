import gc, weakref

__all__ = ['Reference', 'ref', 'deref', 'deref_proxy', 'proxy_ref',
           'dereference_path', 'weak_ref', 'get_weakrefs',
           'get_objects', 'get_referrers', 'get_referents',
           'get_referring_objects', 'get_referent_count',
           'get_referring_type', 'get_referring_types',
           'get_referent_type', 'get_referent_types',
           'get_referent_count_by_type', 'get_referring_count_by_type',
           'get_referring_objects_by_type', 'get_referents_by_type',
           'get_referring_objects_by_type_and_value', 'get_referents_by_type_and_value']

class Reference(object):
    def __init__(self, referent, callback=None):
        self._referent = referent
        self._callback = callback

