import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))

from googlesearch import search

from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import HTTPBasicAuthHandler
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import ProxyHandler
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import HTTPHandler
from urllib.request import HTTPSHandler
from urllib.request import HTTPCookieProcessor
from urllib.request import Request
from urllib.request import urlopen
from urllib.request import urlretrieve

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlencode
from urllib.parse import urljoin
from urllib.parse import quote
from urllib.parse import unquote

from
