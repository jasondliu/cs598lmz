import _struct
import _codecs
import _weakref
import _random
import _bisect
import _heapq
import _hotshot
import _fileio
import _collections
import _ssl
import _sha512
import _sha256
import _sha
import _md5
import _json
import _io
import _crypt
import _bz2
import _struct
import _codecs
import _weakref
import _random
import _bisect
import _heapq
import _hotshot
import _fileio
import _collections

# begin block: zipimport
import zipimport
_zipimport = zipimport

sys.path_hooks.append(_zipimport.zipimporter)
sys.path_importer_cache.clear()

# end block: zipimport

# begin block: site
import site
sys.path[:0] = site.addsitedir(
    os.path.join(os.path.dirname(__file__), 'site-packages'),
    set())

# end block: site

# begin block: encodings

