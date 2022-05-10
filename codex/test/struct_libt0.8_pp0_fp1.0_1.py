import _struct
 
from . import ffi, lib

from iotbx.map_model_manager import map_model_manager
from libtbx import group_args
from mmtbx.validation.ramalyze import ramalyze
from cctbx.maptbx import crystal_gridding
from cctbx.sgtbx import change_of_basis_op
from cctbx import crystal
from cctbx.array_family import flex
from scitbx.array_family import shared
from cctbx import adptbx
from scitbx.math import dihedral_angle

class ramachandran_manager(object):
  def __init__(self, crystal_symmetry, mon_lib_srv, rotamer_eval, mcm):
    self.mcm = mcm
    self.is_phipsi_defined = False
    self.rotamer_eval = rotamer_eval
    self.crystal_symmetry = crystal_symmetry
