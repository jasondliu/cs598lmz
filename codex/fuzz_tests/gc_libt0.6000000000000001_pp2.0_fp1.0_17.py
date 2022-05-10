import gc, weakref
from collections import OrderedDict

from nose.tools import assert_equal, assert_raises

from . import test_env

from .. import vtk_interface
from ..vtk_interface.numpy_support import numpy_to_vtk, vtk_to_numpy
from ..vtk_interface.vtk_interface import (
    vtkPolyData, vtkCellArray, vtkUnsignedCharArray, vtkDoubleArray,
    vtkFloatArray, vtkUnsignedIntArray, vtkPointData, vtkCellData,
    numpy_to_vtkIdTypeArray, vtkIdList)

from ..vtk_interface.decorators import (
    wrap_input, wrap_output, wrap_input_output, wrap_output_rtype)

from ..vtk_interface.algorithms import (
    vtk_points_to_poly_data, vtk_cells_to_poly_data,
    vtk_point_data_to_poly_data, vtk_cell_data_to_poly_data,
    vtk
