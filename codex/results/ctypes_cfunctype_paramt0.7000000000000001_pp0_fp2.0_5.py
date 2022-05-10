import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

from OpenGL.GL import *
import numpy as np
from glfw_window import GLFWWindow
from texture import texture2D
from framebuffer import framebuffer
from shader import program, vertex_shader, fragment_shader
import glm

from PIL import Image

from glfw_window import GLFWWindow

# class MainWindow(GLFWWindow):
#     def __init__(self, w, h, title):
#         super(MainWindow, self).__init__(w, h, title)

#         self.camera = glm.vec3(0.0, 0.0, 3.0)
#         self.lastx = float(self.width)/2
#         self.lasty = float(self.height)/2
#         self.first_mouse = True
#         self.yaw = -90.0
#         self.pitch = 0.0

#         self.delta_time = 0.0
#         self.last_frame = 0.0

#         self.beluga_pos = glm.vec3
