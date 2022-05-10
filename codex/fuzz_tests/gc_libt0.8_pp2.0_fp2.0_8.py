import gc, weakref

from os import path

from itertools import count

from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.logger import Logger

from kivy.graphics import update_normal_mat
from kivy.graphics import Color, Line, Rectangle, Triangle, Mesh, Ellipse
from kivy.graphics.transformation import Matrix

from kivy.graphics.opengl import glPushMatrix, glPopMatrix, glTranslatef, glRotatef, glScalef

from kivy.clock import Clock

from kivy.properties import ListProperty, AliasProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivy.properties import ReferenceListProperty, StringProperty

from kivy.base import EventLoop

import editor
import feature

class Point(Widget):
    """
    The point is the basic structure of the editor, they should link to each other by the joints.
    The points can be moved from their coordinates and rotated from the center of the
