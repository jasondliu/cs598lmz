import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _util
from . import _compat
from . import _html
from . import _html5lib
from . import _lxml
from . import _htmlparser
from . import _beautifulsoup
from . import _sgmlop
from . import _markupbase
from . import _html5lib_py3
from . import _html5lib_py2
from . import _exceptions
from . import _html5builder
from . import _tokenizer
from . import _treewalkers
from . import _sanitizer
from . import _serializer
from . import _constants
from . import _tokenizer_states
from . import _treebuilders
from . import _trie
from . import _filters
from . import _utils
from . import _namespaces
from . import _tokenizer_errors
from . import _treewalkers_validation
from . import _treebuilders_validation
from . import _tokenizer_charsets
from . import _tokenizer_states_initial
from . import _tokenizer
