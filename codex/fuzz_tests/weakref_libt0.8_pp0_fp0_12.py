import weakref

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ETC.constant import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_RESIZABLE
from ETC.renderObject import RenderObject
from ETC.renderObjects import RenderObjects



class Render(object):


	def __init__(self, camera):

		self.camera = camera
		self.lastDrawTime = 0.0

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

		glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
		glutCreateWindow("Elder Tale Time")

		# 색상을 지정할 때, 0부터 1사이의 값을 지정해야 함.
		
