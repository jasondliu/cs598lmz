import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
def beam_h(z):
    """
    Returns half width at the edge of a beam with the given axial 
    size. Assumes a Gaussian beam
    Arguments:
    z:      Axial position in meters. If z is negative, the beam is
            assumed to be truncated by a knife-edge, and returns
            the width of the truncated portion of the beam.
            If z is positive, the function returns the width at that
            point.
    Returns:
    Halfwidth of the beam in the same units as z.
    """
    #Should define the halfwidth at the edge here!
    return 1.e-3   #half width of beam at edge in meters

from lmfit.models import LorentzianModel
from lmfit.models import VoigtModel
from lmfit.models import LinearModel
from lmfit.models import ConstantModel
from lmfit import Model

from . import smithplot
from .smithplot import SmithAxes
from .smithplot import SmithAxes3D
