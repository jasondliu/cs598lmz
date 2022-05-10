import weakref


class WeakTypeMap(object):

    """
    Like builtin types, this will be shared by all values:

        >>> with weakref.all_weakrefs(i for _, i in WeakTypeMap.type_mapping.items()):
        ...     WeakTypeMap.register_type(object, type)

    """
    type_mapping = {t: w for t, w in WeakTypeMap.__dict__.items() if t.endswith('type')}
    type_reverse_mapping = {w: t for t, w in WeakTypeMap.__dict__.items() if t.endswith('type')}

    @classmethod
    def register_type(cls, tkey, tvalue):
        cls.type_mapping[tkey] = tvalue

    @classmethod
    def register_reverse_type(cls, twkey, tkey):
        cls.type_reverse_mapping[twkey] = tkey

    @classmethod
    def get_type(cls, tkey):
        return cls.type_
