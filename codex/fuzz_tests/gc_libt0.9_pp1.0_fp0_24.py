import gc, weakref
import ifcopenshell

from . import ifc_parser
from . import ifc_struct, ifc_schema
from . import ifc_extract
from . import ifc_utils, ifc_geom_api
from . import ifc_guid
from . import ifc_planar_utils

fileCache = {}
tempFileCache = {}
geometryCache = {}

knotStyles = {1:'LINEAR_KNOTS', 2:'UNIFORM_KNOTS', 3:'QUASI_UNIFORM_KNOTS', 4:'PIECEWISE_BEZIER_KNOTS'}
windingModes = {0:'UNSPECIFIED', 1:'CLOCKWISE', 2:'COUNTERCLOCKWISE'}

def freeVertices(l):
  return [FreeCAD.Vector(i) for i in l]

def intangents(c,bc):
  i1 = bc
  i2 = c.Placement.Base.sub(bc)
  return i1, i2

def tangents(
