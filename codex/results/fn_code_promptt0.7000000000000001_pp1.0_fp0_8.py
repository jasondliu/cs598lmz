fn = lambda: None
# Test fn.__code__.co_filename, fn.__code__.co_firstlineno, and fn.__code__.co_name
# TODO: When Python 2.6 is ubiquitous, use inspect.getframeinfo()

def _get_frameinfo():
    # Get the frameinfo object, so we can test it to see if it is valid.
    if sys.version_info >= (3, 2):
        try:
            return sys._getframe()
        except AttributeError:
            return None
    else:
        return sys._getframe()

def _get_codeinfo(frameinfo):
    # Get the codeinfo object, so we can test it to see if it is valid.
    if sys.version_info >= (3, 2):
        try:
            return frameinfo.f_code
        except AttributeError:
            return None
    else:
        return frameinfo.f_code

def _get_func_info(frameinfo):
    # Get the func_info object, so we can test it to see if it is valid.
    if sys.version_info >= (
