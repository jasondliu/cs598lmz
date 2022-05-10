import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time

from pyscf import lib
from pyscf import gto
from pyscf.lib import param
from pyscf.scf import _vhf

if gto.Mole._have_pybel:
    from pyscf.tools.cubegen import get_cell, make_density_map
else:
    get_cell = make_density_map = None


def get_crys_rec(mol, mesg=sys.stdout, coc=None, cell=None, aosym='s4'):
    '''Create crystalline pseudo wavefunction.  The overlap matrix is
    symmetrized to match the symmetry of the given cell.
    '''
    from pyscf.pbc import gto as pbcgto
    from pyscf.pbc import scf as pbcscf
    from pyscf.pbc import df
    from pyscf.pbc.scf import hf as phf
    from pyscf.pbc.scf import khf
    if cell is None:
       
