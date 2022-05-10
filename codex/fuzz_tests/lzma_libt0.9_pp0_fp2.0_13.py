import lzma
lzma.close # just check that it works

PY3 = sys.version_info[0] >= 3

if PY3:
    import urllib.parse as urllib
else:
    import urllib

POWERLINE_ROOT_PATH = Path(__file__).resolve().parents[1]

log = logging.getLogger('powerline.bindings.ipython.install')

CONTENTS_RE = re.compile('<a[^>]+href="([^"]+)"[^>]*>([^<]+)')

V3_EXTENSION_VERSION = "0.4.4"
V4_EXTENSION_VERSION = "0.4.4"

V3_DOWNLOAD_URL = 'https://pypi.python.org/packages/source/p/powerline-status/powerline-status-{version}.tar.gz'
V3_URL = 'https://pypi.python.org/pypi/powerline-status'
V3_ARCHIVE = 'powerline-status-{version}.
