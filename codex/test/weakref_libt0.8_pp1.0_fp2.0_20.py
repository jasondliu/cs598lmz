import weakref

import numpy as np

from climlab import constants as const
from climlab.domain.field import Field
from climlab.utils.thermo import entropy_to_t

O2_c = const.O2_c.copy()
O2_c['units'] = 'ppmv'

