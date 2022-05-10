import codecs
# Test codecs.register_error() here
# type_error ::= str*

def test_register_error():
    try:
        codecs.register_error()
    except TypeError:
        pass
    else:
        raise TestFailed()

# Test codecs.__file__
def test_registration_file():
    assert hasattr(codecs, '__file__'), "codecs has no __file__"

def verify_create_error(name):
    try:
        codecs.lookup_error(name)
        raise ValueError
    except LookupError:
        pass

def verify_register_error(name):
    verify_create_error(name)
    num_errors = len(codecs.error_registry)
    codecs.register_error(name, None)
    assert len(codecs.error_registry) == num_errors
    codecs.register_error(name, None)
    assert len(codecs.error_registry) == num_errors
