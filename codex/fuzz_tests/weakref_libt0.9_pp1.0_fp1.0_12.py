import weakref
import warnings

class ResourceManager(object):
    """
    Resource manager. See the documentation for :ref:`tut-resource-management`.
    """
    def __init__(self):
        self._resources = []

    def __enter__(self):
        warnings.warn("'MyiaResourceManager' is deprecated.", DeprecationWarning)

    def __exit__(self, *args):
        warnings.warn("'MyiaResourceManager' is deprecated.", DeprecationWarning)

    def register(self, resource):
        """Register a new resource.

        Parameters
        ----------
        resource: Resource

        Returns
        -------
        WeakRef
        """
        warnings.warn("'MyiaResourceManager' is deprecated.", DeprecationWarning)
        ref = weakref.ref(resource, self._resources.append)
        self._resources.append(ref)
        return ref

    def deregister(self, resource):
        """Deregister a resource.

        Parameters
        ----------
        resource: Resource
        """
        warnings.warn("'MyiaResourceManager' is
