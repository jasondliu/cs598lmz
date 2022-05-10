import weakref


class CacheManager(object):
    """
    Manage the object instances cache.

    :param klass: Class to manage
    :type klass: class
    """

    def __init__(self, klass):
        self.klass = klass
        self.instances = {}

    def add(self, instance):
        """
        Add an instance to the cache manager.

        :param instance: instance to add
        :type instance: instance
        """
        self.instances[instance.key] = weakref.ref(instance)

    def find(self, key):
        """
        Find an instance by key in cache manager.

        :param key: key of instance to find
        :type key: str
        """
        return self.instances.get(key, lambda: None)()

    def all(self):
        """
        Return all instances in cache manager.
        """
        return [instance() for instance in self.instances.values() if instance() is not None]


class CachedMeta(type):
    """
    Metaclass for cached
