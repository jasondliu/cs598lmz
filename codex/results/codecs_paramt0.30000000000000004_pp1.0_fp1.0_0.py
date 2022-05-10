import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _base

class Base64(_base.Base):
    def __init__(self, *args, **kwargs):
        super(Base64, self).__init__(*args, **kwargs)

    def encode(self, data):
        return base64.b64encode(data)

    def decode(self, data):
        return base64.b64decode(data)

class Base32(_base.Base):
    def __init__(self, *args, **kwargs):
        super(Base32, self).__init__(*args, **kwargs)

    def encode(self, data):
        return base64.b32encode(data)

    def decode(self, data):
        return base64.b32decode(data)

class Base16(_base.Base):
    def __init__(self, *args, **kwargs):
        super(Base16, self).__init__(*args, **kwargs)

    def encode(self, data):
        return base64.
