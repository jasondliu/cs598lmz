fn = lambda: None
# Test fn.__code__.co_flags for 2.6+
try:
    fn.__code__.co_flags
except AttributeError:
    def _is_generator(func):
        return False
else:
    def _is_generator(func):
        return bool(func.__code__.co_flags & CO_GENERATOR)

def _is_generator_function(func):
    return bool(inspect.isgeneratorfunction(func) or _is_generator(func))

def _is_generator_instance(func):
    return bool(inspect.isgenerator(func) or _is_generator(func))

def _is_coroutine(func):
    """
    Returns True if the function is a coroutine.
    """
    return asyncio and asyncio.iscoroutinefunction(func)

def _is_coroutine_function(func):
    """
    Returns True if the function is a coroutine function.
    """
    return asyncio and asyncio.iscoroutinefunction(func)

def _is_coroutine_instance
