import weakref

import numpy as np

from . import _pygimli_ as pg
from . import _pygimli_utils_ as pgutils
from . import _pygimli_mesh_ as pgmesh
from . import _pygimli_core_ as pgcore
from . import _pygimli_modelling_ as pgmod
from . import _pygimli_cmatrix_ as pgcmatrix
from . import _pygimli_fop_ as pgfop
from . import _pygimli_solver_ as pgsolver


def createMesh(x=None, y=None, z=None, tri=None, lines=None,
               marker=None, verbose=False, quality=30.0):
    """Create a mesh from given data.

    Create a mesh from given data.

    Parameters
    ----------
    x : array_like
        x-coordinates of nodes
    y : array_like
        y-coordinates of nodes
    z : array_like
        z-coordinates of nodes
    tri : array
