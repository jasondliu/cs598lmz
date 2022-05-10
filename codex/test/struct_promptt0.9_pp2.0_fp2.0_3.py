import _struct
# Test _struct.Struct().format (Issue #17406)
# Code from functools.update_wrapper()
def update_wrapper(wrapper,
     wrapped,
     assigned =functools._WRAPPER_ASSIGNMENTS,
     updated =functools._WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)

    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, ()))
    wrapper.__wrapped__ = wrapped
    return wrapper


def update_wrapper(wrapper,
     wrapped,
     assigned =functools._WRAPPER_ASSIGNMENTS,
     updated =functools._WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
