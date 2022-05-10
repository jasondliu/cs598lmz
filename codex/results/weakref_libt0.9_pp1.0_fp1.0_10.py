import weakref

_logger = logging.getLogger(__name__)


def _warn_for_invalid_proxy(app, root, atom_value='#ValidIf_0'):
    """Check for proxies that are invalid since the last server idle callback.
    """
    app.proxies.warn_if_invalid(root, atom_value=atom_value)


def _clean_for_invalid_proxy(app, root, atom_value='#ValidIf_0'):
    """Check for proxies that are invalid since the last server idle callback.
    """
    app.proxies.clean_if_invalid(root, atom_value=atom_value)


def _release_object(app, atom_value, function=None):
    """Release an object, preventing the event handlers from that object
    from running more. An error message is logged if the object is not
    present.

    """
    obj = app._get_object(atom_value)
    if not obj or not atom_value == getattr(obj, 'atom_value', None):
        _
