import io
class File(io.RawIOBase):
  pass

#-----------------------------------------------------------------------------
# Built-in types.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------
class Action(object): pass
class Tensor(object): pass
class Dataset(object): pass
class tf(object):
  def function(self, input_signature=None):
    """Decorator to mark a function as a TensorFlow function.
    """
    def _guarded_noarg_decorator(func):
      return func
    if input_signature is None:
      # Simple decorator that adds the `tf.function` attribute to the function.
      return _guarded_noarg_decorator
    else:
      def _decorator(func):
        # Add an attribute to the func indicating that it's a tf.function.
        # This is used by various tooling.
        func.__dict__['_is_tf_function'] = True
        return func
      return _decorator

def abort_handler(self, *args, **kwargs):
    raise Exception('abort_handler')


