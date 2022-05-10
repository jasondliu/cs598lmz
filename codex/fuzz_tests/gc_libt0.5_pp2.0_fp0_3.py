import gc, weakref
from collections import namedtuple
from collections.abc import Iterable
from functools import reduce
from itertools import chain
from operator import or_
from operator import and_
from typing import List, Tuple, Optional, Iterator, Sequence, Set, Union

from . import _constants as const
from . import _util as util
from . import _exceptions as exc
from . import _props as props
from . import _hints as hints
from . import _bases as bases
from . import _tiles as tiles
from . import _tiles_collection as tiles_collection
from . import _puzzle as puzzle
from . import _puzzle_collection as puzzle_collection
from . import _puzzle_props as puzzle_props
from . import _puzzle_collection_props as puzzle_collection_props
from . import _puzzle_collection_props_mixins as puzzle_collection_props_mixins
from . import _puzzle_collection_props_mixins_abc as puzzle_collection_props_mixins_abc
from . import _puzzle_collection
