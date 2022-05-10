import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _common
from . import _compat
from . import _exceptions
from . import _filesystem
from . import _logging
from . import _options
from . import _os
from . import _process
from . import _python
from . import _repository
from . import _subprocess
from . import _system
from . import _url
from . import _util
from . import _version

from ._common import *
from ._compat import *
from ._exceptions import *
from ._filesystem import *
from ._logging import *
from ._options import *
from ._os import *
from ._process import *
from ._python import *
from ._repository import *
from ._subprocess import *
from ._system import *
from ._url import *
from ._util import *
from ._version import *

from ._common import __version__

from ._logging import log

from ._util import get_default_encoding
from ._util import get_default_locale
from ._util import get_default_
