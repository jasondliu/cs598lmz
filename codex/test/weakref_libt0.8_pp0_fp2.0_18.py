import weakref
import mathutils

from sverchok.utils.logging import debug, info
from sverchok.utils.geom import centroids_of_faces
from sverchok.ui.sv_icons import custom_icon
from sverchok.utils.nodes_dict import set_and_create_nodes_dict
from sverchok.utils.geom import multipliers
from sverchok.utils.geom import apply_matrix_to_vector_list
from sverchok.utils.geom import Matrix_generate
from sverchok import old_nodes

def recalculate_mesh(self, context):
    ## recomputes the geometry.
    ob = old_nodes.mk_geom_obj()
    me = ob["me"]
    for i in range(len(self.verts_u)):
        me.vertices.add(len(self.verts_u[i]))
