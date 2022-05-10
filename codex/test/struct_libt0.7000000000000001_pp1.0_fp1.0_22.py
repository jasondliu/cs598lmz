import _struct

from .. import util
from .. import constants
from .. import config
from .. import matrices
from .. import debug
from .. import nodes

# -----------------------------------------------------------------------------

class Direct(object):

    def __init__(self, ):
        self.vertices = []
        self.colors = []
        self.texcoords = []
        self.normals = []
        self.indices = []
        self.count = 0
        self.mode = 0
        self.primgroup = 0

        self.gl_vbo = None
        self.gl_ibo = None

    def set_mode(self, mode):
        self.mode = mode

    def set_primgroup(self, primgroup):
        self.primgroup = primgroup

    def get_count(self, ):
        return self.count

    def set_count(self, count):
        self.count = count

    def set_indices(self, indices):
        self.indices = indices

    def add_vertex(self, point):
        self.vertices.append(point)

   
