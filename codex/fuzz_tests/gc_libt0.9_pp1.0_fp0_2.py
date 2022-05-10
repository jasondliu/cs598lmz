import gc, weakref

__all__ = ['Notifier', 'NotifierConfig', 'NotifierConfigRef']

class NotifierConfigRef(weakref.WeakSet):
    """ Weak reference helper class.
    NotifierConfigRef is accessible as an attribute of NotifierConfig instances.
    This is used to collect references to those instances,
    and to delete them when the Notify is destroyed.
    """

class NotifierConfig(object):

    def __init__(self, notify, type, id = None):
        self._ref = NotifierConfigRef()
        self._ref.add(notify)
        if id:
            self._id = id
        else:
            self._id = "notifier_%s" % str(id(self))
        self._info = notify._driver.get_info(type, self._id)
        
        # If get_info returns None, that indicates the service
        # or protocol is not supported on this platform.
        if self._info == None:
            raise RuntimeError
        self._trigger = notify._driver.get_trigger(type, self._id)


