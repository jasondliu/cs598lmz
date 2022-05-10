import weakref
import sys

__all__ = ['add_default_handler']

_default_handlers = []

def add_default_handler(handler):
    """Add a handler to the list of default handlers.

    Default handlers are called when no other handlers handle an event.
    """
    if isinstance(handler, weakref.ProxyType):
        handler = handler.__wrapped__
    if handler in _default_handlers:
        raise ValueError("handler already in default handlers")
    _default_handlers.append(handler)

def remove_default_handler(handler):
    """Remove a handler from the list of default handlers."""
    try:
        _default_handlers.remove(handler)
    except ValueError:
        pass

def get_default_handlers():
    """Get a list of the default handlers."""
    return _default_handlers[:]

