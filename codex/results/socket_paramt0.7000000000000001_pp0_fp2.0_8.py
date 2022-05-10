import socket
socket.if_indextoname(4)
socket.if_nametoindex('en0')

import os
print(os.getcwd())
os.chdir('./Documents')
print(os.getcwd())
os.chdir('../Downloads')
print(os.getcwd())

os.path.join('usr', 'bin', 'spam')
os.path.join('usr', 'bin', 'spam')

import glob
glob.glob('*.py')

from typing import *

from typing import List, Tuple, Sequence, Iterable, Container, Sized, Callable, Any, Union, TypeVar, Type, Set
from typing import NewType

from typing import NamedTuple

from typing import Optional
from typing import Generic, Iterator
from typing import Counter
from typing import cast

from typing import ClassVar
from typing import no_type_check, no_type_check_decorator
from typing import typevar
from typing import Literal
from typing import Protocol
from typing import runtime_checkable
from typing import ForwardRef
from typing import Annotated
from
