import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def empty_callback():
    pass

glfw.Init()
glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.WindowHint(glfw.RESIZABLE, GL_FALSE)
glfw.WindowHint(glfw.DOUBLEBUFFER, GL_TRUE)

window = glfw.CreateWindow(WIDTH, HEIGHT, "LearnOpenGL", None, None)
glfw.SetWindowPos(window, 400, 200)
glfw.MakeContextCurrent(window)

glViewport(0, 0, WIDTH, HEIGHT)

glfw.SetKeyCallback(window
