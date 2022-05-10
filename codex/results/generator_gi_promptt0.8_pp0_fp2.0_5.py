gi = (i for i in ())
# Test gi.gi_code.co_freevars
if hasattr(gi, 'gi_code'):
    gi_code_freevars = gi.gi_code.co_freevars
else:
    gi_code_freevars = None


def gen_cls(self, **kwargs):
    """
    Class decorator to generate a well-behaved class.

    Needed since ``type`` is broken.

    """
    return cls_cls(self.__name__, (self, ), kwargs)


def _assert_is_instance_or_subclass(arg, cls):
    if isinstance(arg, cls):
        return
    if not issubclass(arg, cls):
        raise TypeError('%s is not a subclass of %s' % (arg, cls))


def _assert_string_or_iterable(names):
    if isinstance(names, six.string_types):
        return
    if hasattr(names, '__iter__'):
        return
    raise TypeError("'names' must be
