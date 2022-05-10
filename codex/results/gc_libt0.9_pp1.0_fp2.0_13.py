import gc, weakref
from mh_utils import BoundingBox, invertX
from mh.render import Geometry3D
from mh import mathutil
from numpy import array, zeros, arange, concatenate, amax, amin, any, all

from skeleton import Joint, VertexJointWeights, Cylinder, Bone
from animation import Pose

from mh.render import Mesh, Color
import mh2skn as cor

class HumanGeometry(object):
    '''
    classdocs
    '''
    def __init__(self, filepath, config=None):
        '''
        Constructor
        '''
        self.nVertices = 0
        self.nFaces = 0

        self.vertexCoords = None
        self.faceNormalCoords = None
        self.faceVertices = None
        self.vnormals = None
        self.fnormals = None

        self.texVerts = None
        self.vertexGroups = None
        self.uvValues = None

        self.materials = None
        self.
