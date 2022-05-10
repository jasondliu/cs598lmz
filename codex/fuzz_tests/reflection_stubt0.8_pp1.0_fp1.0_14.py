fn = lambda: None
gi = (i for i in ())
fn.__code__ = coro
gi.gi_code = coro


# Run

def _run(coro, *args):
    try:
        coro.send(None)
        coro.send(*args)
    except StopIteration as e:
        return e.value


def _run_fn(fn, *args):
    try:
        fn(*args)
    except StopIteration as e:
        return e.value


run = _run if PY3 else _run_fn


# Testing

def _unmock_cancellations():
    """
    Unmock the cancellation mechanism for the most part.
    """
    for (obj, attname) in _cancellable_attributes:
        setattr(obj, attname, _original_cancellable_attrs[obj, attname])
    _original_cancellable_attrs.clear()
    _cancellable_attributes.clear()


def _cancel_mock(mock):
    """
    Mock a generator to execute a cancellation.
    """
