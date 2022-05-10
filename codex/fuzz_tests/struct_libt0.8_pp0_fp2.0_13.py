import _struct_residue
import _struct_chain

import _struct_mol

import _struct

class struct_helper:
    def __init__(self):
        self.atom = _struct_atom.struct_atom_helper()
        self.residue = _struct_residue.struct_residue_helper()
        self.chain = _struct_chain.struct_chain_helper()

        self.mol = _struct_mol.struct_mol_helper()

        self.struct = _struct.struct_helper()

# _struct_list.py
#
# michel.michaud@cnrs-orleans.fr
# 2016-08-16
#

from psrchive import Archive
import numpy as np

from _util import *

def set_struct_list_from_archive(s, arch):
    '''
    set structure from psrchive Archive arch
    '''
    beam_idx = arch.get_beam_index()
    nbeams = arch.get_nbeams()

