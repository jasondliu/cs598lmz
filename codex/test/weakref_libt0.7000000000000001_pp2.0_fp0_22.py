import weakref

import numpy as np

from scipy.sparse import coo_matrix, csc_matrix, csr_matrix, spdiags, \
    dia_matrix, isspmatrix, dok_matrix

from mathkit.matrix_la.sys_mtx_assembly import SysMtxAssembly

from ibvpy.api import BCDof, \
    RTraceGraph, RTraceDomainListField, TLoop, \
    TStepper as TS, TLine, BCDofGroup, IBVModel

from ibvpy.mats.mats2D.mats2D_elastic.mats2D_elastic import MATS2DElastic

from ibvpy.mats.mats3D.mats3D_elastic.mats3D_elastic import MATS3DElastic

# from ibvpy.mats.matsXD.matsXD_cmdm.matsXD_cmdm import MATSXDMicroplaneDamage
# from matsXD_cmdm_
