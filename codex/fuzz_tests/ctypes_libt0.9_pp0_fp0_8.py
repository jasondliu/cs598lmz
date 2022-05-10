import ctypes
ctypes.windll.kernel32.SetDllDirectoryW(os.path.join(os.getcwd(),"dll"))
import platform, sys
if platform.architecture()[0] == '32bit':
    os.environ['PATH'] += ';'+os.getcwd()+';'+os.getcwd()+'\\dll\\x86'
else:
    os.environ['PATH'] += ';'+os.getcwd()+';'+os.getcwd()+'\\dll\\x64'
import numpy as np

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL.raw.GL.VERSION.GL_1_0 import glViewport
from objloader import *


class OBJLoader:
    def __init__(self, path):
        self.vert_coords = []
        self.text_coords = []
        self.norm_coords = []

        self.vertex_index = []
        self.texture_
