import threading
threading.stack_size(2**27)

import sys
import pyglet
from pyglet.window import key
import ratcave as rc

# Read Wavefront OBJ
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)
monkey_obj = obj_reader.get_mesh("Monkey", position=(0, 0, -2))
monkey_obj.uniforms['diffuse'] = 1., 1., 0.
monkey_obj.uniforms['flat_shading'] = False
monkey_obj.uniforms['specular'] = 0.5, 0.5, 0.5
monkey_obj.uniforms['shininess'] = 5.

# Read Wavefront OBJ
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)
cube_obj = obj_reader.get_mesh("Cube", position=(0, 0, -2))
cube_obj.uniforms['diffuse'] = 0., 0.5, 0.
cube
