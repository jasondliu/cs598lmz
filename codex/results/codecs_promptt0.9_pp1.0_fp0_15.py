import codecs
# Test codecs.register_error ctor
class CodecsRegError1(codecs.RegisterError):
    pass
# Test codecs.register_error ctor
class CodecsRegError2(Exception):
    __qualname__ = 'CodecsRegError2'
    def __init__(self, obj, encoded=None, reason='reason'):
        super().__init__()
        self.obj = obj
        self.encoded = encoded
        self.reason = reason
class CodecsRegError3(Exception):
    __qualname__ = 'CodecsRegError3'
    def __init__(self, obj, encoded=None, reason='reason'):
        self.obj = obj
        self.encoded = encoded
        self.reason = reason
        super().__init__()
codecs.register_error('cerror1', CodecsRegError1)
codecs.register_error('cerror2', CodecsRegError2)
codecs.register_error('cerror3', CodecsRegError3)
codecs.register_error('cerror4', 'Exception')

