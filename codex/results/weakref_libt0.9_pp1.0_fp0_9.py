import weakref

DEFAULT_MAX_MESSAGES_TO_KEEP = 20

log = logging.getLogger(__name__)


class _GlobalInstanceType(type):
    """
    Allows only a single instance of an object, by reducing the new object to a
    weak reference.

    This type is mostly useful for object which represent an object that
    exists in a process-wide context. e.g. a QApplication instance (only one
    allowed).
    """
    def __call__(cls, *args, **kwargs):
        try:
            ref = cls.__instance.__call__()
        except AttributeError:
            ref = None

        if not ref:
            newInst = super(_GlobalInstanceType, cls).__call__(*args, **kwargs)
            cls.__instance = weakref.ref(newInst)
        # else:
            # TODO: add sensible warning here
        return cls.__instance()


class _MessageBuffer(object):
    """
    The message buffer is a queue of message with size limit, it keeps
