import weakref

from . import dbus_proxy_base, dbus_signal_emitter, \
    dbus_service, session_bus

from decorator import decorator

class DBusProxy(dbus_proxy_base.DBusProxyBase):
    """DBus proxy object, to be used with the @dbus_proxy decorator.

    This is a normal python object with two extra features:
    - dbus methods' parameters may be annotated to give a dbus signature
    - when a dbus method is called, the property '_on_dbus_call' is set
      with the current execution context (see dbus_service)

    Note that DBusProxy objects cannot store non-pickable objects.
    """

    def __init__(self, interface, bus=None):
        """Create a DBusProxy object.

        interface -- The object will act as proxy for the service
           defined by this interface.
        bus -- A dbus.SessionBus() object or something similar,
           identifying the bus the proxy should use
        """
        if bus == None:
            bus = session_bus
