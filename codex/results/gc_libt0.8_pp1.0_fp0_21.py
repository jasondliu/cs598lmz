import gc, weakref
import itertools
from collections import OrderedDict

from kivy.graphics import InstructionGroup
from kivy.graphics.instructions import RenderContext, Callback
from kivy.graphics.opengl import glGetInteger, GL_CULL_FACE_MODE, \
    GL_FRONT_FACE, GL_FRONT, GL_CW, GL_BACK, GL_CCW
from kivy.graphics.stencil_instructions import StencilPush, StencilPop
from kivy.graphics.transformation import Matrix
from kivy.utils import QueryDict
from kivy.resources import resource_find


if platform == 'android':
    from jnius import autoclass, cast
    from android import activity
    from android.runnable import run_on_ui_thread
else:
    def run_on_ui_thread(x):
        return x


# This shader works in two stages, first is to apply the first transformation
# (the one applied at the beginning of the canvas) to all vertices.
#
