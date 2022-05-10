import weakref
from collections import defaultdict

import numpy as np
import pandas as pd

from . import utils
from . import xr_utils
from . import plotting
from . import xr_utils as xru
from . import xr_time as xt
from . import xr_geo as xg
from . import xr_stats as xs
from . import xr_interp as xi
from . import xr_extras as xe
from . import xr_dataset as xd
from . import xr_transform as xtr
from . import xr_select as xsel
from . import xr_concat as xcon
from . import xr_roll as xroll
from . import xr_resample as xres
from . import xr_reduce as xred
from . import xr_groupby as xgb
from . import xr_agg as xagg
from . import xr_apply as xapply
from . import xr_intersect as xint
from . import xr_reindex as xreindex
from . import
