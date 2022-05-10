import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db').execute('SELECT * FROM test')

# test text
#t = '''\
#abcde
#abcdef
#'''

def gl_gettext(num_chars):
    '''
    returns num_chars from the gl text buffer
    '''
    buf = ctypes.create_string_buffer(b'\0'*num_chars)
    glReadBuffer(GL_FRONT)
    glReadPixels(0, 0, num_chars, 1, GL_RGBA, GL_UNSIGNED_BYTE, buf)
    return buf.value

def get_glfw_func(name, restype, argtypes):
    '''
    returns a ctypes function from the glfw dll
    '''
    f = glfw.glfwGetProcAddress(name)
    f.restype = restype
    f.argtypes = argtypes
    return f

#
# opengl functions
#

glfw.glfwInit()

glfw.glfwOpenWindow
