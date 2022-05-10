import _struct

from . import _common
from . import _compat
from . import _util
from . import _vendor
from . import _vendor_six as _six
from . import _vendor_urllib3 as _urllib3
from . import exceptions

try:
    from typing import Any
    from typing import Callable
    from typing import Dict
    from typing import Iterator
    from typing import List
    from typing import Optional
    from typing import Tuple
    from typing import Type
    from typing import Union
except ImportError:
    pass

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from . import _types
    from . import _vendor_urllib3 as _urllib3
    from . import _vendor_urllib3 as _urllib3
    from . import _vendor_urllib3 as _urllib3
    from . import _vendor_urllib3 as _urllib3
    from . import _
