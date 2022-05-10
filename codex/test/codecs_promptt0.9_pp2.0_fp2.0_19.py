import codecs
# Test codecs.register_error once to make sure it is really available if we need
# it (used in normalize()). The user might have the codecs module but not have
# the platform C runtime library installed, in which case the registrering will
# fail with an AttributeError.
try:
    codecs.register_error('test', lambda x: 42)
except AttributeError:
    # We're likely running on App Engine where codecs.register_error is not
    # available.
    _register_error = None
else:
    _register_error = codecs.register_error


