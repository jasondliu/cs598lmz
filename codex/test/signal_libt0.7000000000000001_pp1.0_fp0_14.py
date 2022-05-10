import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# --------------------------

from PySide import QtCore, QtGui

import FreeCAD
import FreeCADGui
import Part, PartGui
#import Mesh
#import MeshPart
#import MeshPartGui
import Draft
import DraftGui
#import Sketcher
import Drawing
import DrawingGui

def makeArrow(sketch, p1, p2, name, color=None):
    d = Part.Line(p1, p2).toShape()
    if color:
        d.ViewObject.LineColor = color
    return sketch.addGeometry(d,False)

def makeBox(sketch, p1, p2, name, color=None):
    d = Part.makeBox(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z, p1)
    if color:
        d.ViewObject.ShapeColor = color
