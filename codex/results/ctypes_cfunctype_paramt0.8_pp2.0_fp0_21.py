import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class PyEventReceiver(EventReceiver):
    """
    PyEventReceiver - Provides a Python wrapper for Irrlicht's EventReceiver

    Usage:
    -------------------------
    >>> def inputevent(event):
    >>>     # I want to handle this event
    >>>     if event.EventType == irr.EET_MOUSE_INPUT_EVENT:
    >>>         if event.MouseInput.Event == irr.EMIE_LMOUSE_PRESSED_DOWN:
    >>>             print "Left mouse button pressed, we listen to this event"
    >>>             # this event should be handled, so we return True
    >>>             return True

    >>> receiver=PyEventReceiver()
    >>> receiver.OnEvent=inputevent

    >>> device.setEventReceiver(receiver)
    >>> # ...

    """
    def __init__(self):
        EventReceiver.__init__(self)
        self._OnEvent = FUNTYPE()

    def OnEvent(self, event):
        if self._OnEvent:
            return self._
