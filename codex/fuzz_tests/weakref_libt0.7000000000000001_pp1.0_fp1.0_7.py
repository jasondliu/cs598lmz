import weakref

from gaphor.core import eventmanager
from gaphor.core.eventmanager import Event
from gaphor.core.modeling import Presentation

class Notification(object):
    """Notification base class."""

    def __init__(self, subject, property, value=None):
        if isinstance(subject, Presentation):
            subject = subject.subject
        self.subject = subject
        self.property = property
        self.value = value


class ActionExecuted(Notification):
    """Notification for action execution."""

    def __init__(self, action, subject=None, property=None, value=None):
        assert action
        if not subject:
            subject = action.element
        if not property:
            property = 'action'
        Notification.__init__(self, subject, property, value)
        self.action = action


_listeners = weakref.WeakValueDictionary()


class Listener(object):
    """
    A Listener is notified when an event has been sent through the
    EventManager.

    The listener can listen
