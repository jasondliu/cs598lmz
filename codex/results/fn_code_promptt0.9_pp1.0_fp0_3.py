fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = os.path.realpath("<_frozen_importlib_external._Path.rstrip>")
# Test fn.__code__.co_flags
import inspect
fn.__code__.co_flags = (inspect.CO_VARARGS
                         | inspect.CO_VARKEYWORDS
                         | inspect.CO_NESTED
                         | inspect.CO_GENERATOR
                         | inspect.CO_OPTIMIZED
                         | inspect.CO_NEWLOCALS
                         | inspect.CO_NOFREE)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ("a", "b")
# Prints: (22, 20, 4, 4, 0, 0, 1, 0, 0)
print((fn.__code__.co_argcount,
      fn.__code__.co_kwonlyargcount,
      fn.__code__.co_nlocals,
      fn.__code__.co_stacksize,
      fn
