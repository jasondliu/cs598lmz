import gc, weakref
import numpy as np
import numpy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import scipy.optimize as so

from . import _core
from . import _core_c
from . import _core_py
from . import _core_np
from . import _core_np_c
from . import _core_np_py

from . import _core_np_la
from . import _core_np_la_c
from . import _core_np_la_py

from . import _core_np_la_sla
from . import _core_np_la_sla_c
from . import _core_np_la_sla_py

from . import _core_np_la_sla_so
from . import _core_np_la_sla_so_c
from . import _core_np_la_sla_so_py

from . import _core_np_la_sla_so_sp
from . import _core
