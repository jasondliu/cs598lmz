import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _version
from . import _compat
from . import _util
from . import _file
from . import _process
from . import _url
from . import _html
from . import _http
from . import _http_cookiejar
from . import _http_cookiejar_lwp
from . import _http_cookiejar_mozilla
from . import _http_cookiejar_netscape
from . import _http_cookiejar_rfc2965
from . import _http_cookiejar_test
from . import _http_cookiejar_test_mozilla
from . import _http_cookiejar_test_netscape
from . import _http_cookiejar_test_rfc2965
from . import _http_cookiejar_test_rfc6265
from . import _http_cookiejar_test_rfc2109
from . import _http_cookiejar_test_rfc2109_strict
from . import _http_cookiejar_test_rfc2109_strict_domain
from . import _http_cookiejar
