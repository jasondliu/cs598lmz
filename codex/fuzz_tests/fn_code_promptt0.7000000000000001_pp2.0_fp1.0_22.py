fn = lambda: None
# Test fn.__code__.co_flags & 0x20: return fn.__code__.co_flags & 0x20
# Test fn.__code__.co_argcount: return fn.__code__.co_argcount

# End feature tests

def _assert_features():
    def _sig(f):
        return signature(f)

    def _sig_st(f):
        return signature(f).__str__()

    def _sig_iter(f):
        return signature(f).__iter__()

    if not hasattr(inspect, 'Signature'):
        raise AssertionError('inspect.Signature not supported in this build')
    elif not hasattr(inspect, 'signature'):
        raise AssertionError('inspect.signature not supported in this build')

    if not hasattr(_sig(foo), '__str__'):
        raise AssertionError('Signature.__str__ not supported in this build')
    elif not hasattr(_sig(foo), '__iter__'):
        raise AssertionError
