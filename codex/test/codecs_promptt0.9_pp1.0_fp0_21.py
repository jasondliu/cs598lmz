import codecs
# Test codecs.register_error(), codecs.lookup_error()
codecs.register_error('test.lookuperror', codecs.lookup_error)
codecs.lookup_error('test.lookuperror')

class encode:
    def __init__(self, errors='strict'):
        self.errors = errors
        pass
    def encode(self, input, errors=None):
        if errors is None:
            errors = self.errors
        return errors.encode(input, errors)

codecs.register_error('test.encode', encode)
