import mmap
import os
from random import shuffle
from collections import namedtuple

from ursina import *
from ursina.prefabs.model_importer import ModelImporter
from ursina.prefabs.first_person_controller import FirstPersonController

from . import map_format
import perlin


class Map:
    quad_vertex_shader = '''
    #version 330

    layout(location = 0) in vec3 in_position;
    layout(location = 1) in vec3 in_normal;
    layout(location = 2) in vec3 in_uv;
    layout(location = 3) in vec3 in_color;

    out vec3 v_position;
    out vec3 v_normal;
    out vec3 v_uv;
    out vec3 v_color;

    void main() {
        v_position = in_position;
        v_normal = in_normal;
        v_uv = in_uv;
        v_color = in_color;
    }
    '''

    quad_fragment_shader = '
