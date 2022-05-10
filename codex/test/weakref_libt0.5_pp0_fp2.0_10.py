import weakref

from . import config
from . import log
from . import utils
from . import version

# Set the default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())

#: Version number of the :mod:`pywbem` package.
__version__ = version.__version__

#: :term:`WBEM server` :term:`URL`s of public :term:`WBEM server`s.
PUBLIC_WBEM_SERVERS = config.PUBLIC_WBEM_SERVERS

#: Boolean indicating whether the :mod:`pywbem` package is running in Python 3.
PY2 = sys.version_info[0] == 2

#: Boolean indicating whether the :mod:`pywbem` package is running in Python 2.
PY3 = sys.version_info[0] == 3

#: Boolean indicating whether the :mod:`pywbem` package is running in Python 3.4
#: or later.
