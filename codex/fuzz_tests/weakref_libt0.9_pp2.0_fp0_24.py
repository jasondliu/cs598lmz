import weakref

try:
    import sas.realspace.magnetic_scatterers as msc
except:
    print('WARNING: Cannot load magnetic sasmodels')
    import sas.models.background1D as msc

import sas.qtgui.UnitConverter as UnitConverter

from sas.qtgui.Perspectives.Meshes.MeshUtils import MeshPlotData, numericSort
from sas.qtgui.Perspectives.Meshes.MeshManager import MeshModel
from sas.qtgui.Perspectives.Meshes.SubMeshesManager import SubMeshesModel
from sas.qtgui.Perspectives.Meshes.SubMeshesManager import SubMeshesWidget
import sas.qtgui.Utilities.GuiUtils as GuiUtils

import sas.sascalc.data_util.nxsunit as nxsunit

from sas.sasgui.guiframe.dataFitting import Data1D
from sas.sasgui.guiframe.dataFitting import Data2D
