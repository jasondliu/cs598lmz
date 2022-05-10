import codecs
# Test codecs.register_error
def test_register_error():
    class X(Exception):
        pass
