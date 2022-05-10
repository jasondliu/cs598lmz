import ctypes
ctypes.cdll.LoadLibrary('libGL.so')
import OpenGL.GL as GL


class GLTest(unittest.TestCase):
    def test_constants(self):
        GL.GL_NO_ERROR
        GL.GL_LINES
        GL.GL_DEPTH_TEST

    def test_glBegin(self):
        GL.glBegin(GL.GL_LINES)
        GL.glVertex2f(1, 2)
        GL.glVertex2f(3, 4)
        GL.glEnd()

    def test_glDraw(self):
        GL.glDrawArrays(GL.GL_LINES, 0, 2)

    def test_glClearColor(self):
        GL.glClearColor(0.0, 1.0, 0.0, 1.0)

    def test_glClear(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    def test_glEnable(self):
        GL.glEnable(GL.GL_DEPTH_TEST)

    def test_glGet
