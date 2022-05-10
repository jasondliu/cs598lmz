import mmap
import struct

import numpy as np
import pytest

from pyFAI.azimuthalIntegrator import AzimuthalIntegrator
from pyFAI.calibrant import Calibrant
from pyFAI.common import float_, int_, pyFAIException
from pyFAI.geometryRefinement import GeometryRefinement
from pyFAI.mask import Mask
from pyFAI.units import hc
from pyFAI.utils import units, deprecation
from pyFAI.utils.decorators import deprecated
from pyFAI.utils.exceptions import PyFAIException
from pyFAI.utils.splitBBox import splitBBox
from pyFAI.utils.testutils import assert_warns
from pyFAI.geometryRefinement.refinement import RefinementMethod

# try to import fabio
try:
    import fabio
except ImportError:
    fabio = None

# this is the reference geometry
ai_ref = AzimuthalIntegrator()
ai_ref.setFit2D(1000, 1000 * 0.1, 1000 * 0
