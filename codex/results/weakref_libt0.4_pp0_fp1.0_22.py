import weakref

import numpy as np

from . import _pyntcloud
from .utils import (
    get_mesh_vertices_and_faces,
    get_mesh_vertices_and_faces_from_ply,
    get_mesh_vertices_and_faces_from_obj,
    get_mesh_vertices_and_faces_from_off,
    get_mesh_vertices_and_faces_from_npy,
    get_mesh_vertices_and_faces_from_stl,
    get_mesh_vertices_and_faces_from_tri,
    get_mesh_vertices_and_faces_from_dae,
    get_mesh_vertices_and_faces_from_gltf,
    get_mesh_vertices_and_faces_from_glb,
    get_mesh_vertices_and_faces_from_3ds,
    get_mesh_vertices_and_faces_from_blend,
    get_mesh_vertices_and_faces
