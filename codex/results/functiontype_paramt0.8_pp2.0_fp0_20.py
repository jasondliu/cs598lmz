from types import FunctionType
list(FunctionType(lambda: (yield from range(10))).__code__.co_freevars)

# closes #191
b = [1, 2, 3]
list(reversed(b))

# closes #295
from collections import abc
import six

isinstance(b"'", (six.binary_type, six.text_type, abc.Bytes, abc.ByteString, abc.Char))
isinstance(b"batata", (six.binary_type, six.text_type, abc.Bytes, abc.ByteString, abc.Char))

# closes #266
from datetime import time, datetime

datetime.combine(datetime.today(), time(0, tzinfo=datetime.now().tzinfo))
datetime.combine(datetime.utcnow(), time(0))

# closes #263
from shutil import copyfile

copyfile.__code__.co_varnames
copyfile.__code__.co_argcount

# closes #294
class Alias(object):

    def __init
