import mmap

from struct import pack, unpack

from pychemia import pcm_log, HAS_PYCRYSTAL
from pychemia.utils.computing import itertools
from pychemia.code.vasp.kpoints import Kpoints
from pychemia.utils.mathematics import euler_angles_to_rotation_matrix

if HAS_PYCRYSTAL:
    from pycrystal import crystal

logger = pcm_log()


class POSCAR(object):
    def __init__(self, structure=None, nat=None, ntypat=None, typat=None, xred=None, forces=None,
                 stress=None, efermi=None, eigenvalues=None, occupations=None, path='.',
                 xcart=None, avec=None, znucl=None, title=None):

        if structure is not None:
            self.xcart = structure.reduced2cartesian
            self.avec = structure.lattice.matrix
            self.nat = np.array(structure
