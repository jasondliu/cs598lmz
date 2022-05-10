import weakref

class _CachedProperty(object):
    """
    Descriptor (non-data) for building an attribute on-demand on first use.
    """

    def __init__(self, factory):
        """
        <factory> is called such: factory(instance) to build the attribute.
        """
        self._attr_name = factory.__name__
        self._factory = factory

    def __get__(self, instance, owner):
        # Build the attribute.
        attr = self._factory(instance)

        # Cache the value; hide ourselves.
        setattr(instance, self._attr_name, attr)

        return attr

class _LazyDescriptor(object):
    """
    Descriptor for building an attribute on-demand on first use.

    Unlike CachedProperty, _LazyDescriptor is not designed to cache the
    attribute once it has been created. Rather, it is intended to hide
    itself and expose only the attribute.
    """

    def __init__(self, factory):
        """
        <factory>
