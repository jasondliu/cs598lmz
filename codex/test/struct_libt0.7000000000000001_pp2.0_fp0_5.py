import _struct
from . import _common
from . import _errors
from . import _objects
from . import _text
from . import _variables
from . import _view
from . import _config

#-------------------------------------------------------------------------------
class _ProbeSettings(_view.ViewSettings):
    def __init__(self, parent, axis, probe_type, probe_spacing, probe_diameter,
                 probe_length, probe_offset, probe_show_mesh_edges,
                 probe_show_mesh_faces, probe_show_probe_spacing,
                 probe_sphere_resolution, probe_cylinder_resolution):
        self.__parent = parent
        self.__axis = axis
        self.__probe_type = probe_type
        self.__probe_spacing = probe_spacing
        self.__probe_diameter = probe_diameter
        self.__probe_length = probe_length
        self.__probe_offset = probe_offset
        self.__probe_show_mesh_edges = probe_show_mesh_edges

