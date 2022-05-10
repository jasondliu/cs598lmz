import gc, weakref
from collections import defaultdict
from itertools import chain

from . import _py3compat
from . import _util
from . import _compat
from . import _collections_abc
from . import _weakref

from . import _weakrefset
from . import _weakkeydict
from . import _weakref_ref
from . import _weakref_proxy
from . import _weakref_finalize
from . import _weakref_helper
from . import _weakref_backport

from ._util import _format_finalizer_type_and_obj
from ._util import _format_callback_source
from ._util import _format_callback_type_and_obj
from ._util import _format_callback_func_and_args
from ._util import _format_callback_func_and_args_and_kwargs
from ._util import _format_callback_func_and_args_and_keywords
from ._util import _format_callback_func_and_args_and_keywords_and_kwargs
from ._util import _format_callback_func_and_args
