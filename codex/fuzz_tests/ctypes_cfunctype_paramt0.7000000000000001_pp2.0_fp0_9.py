import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int)

class Window(object):
    def __init__(self, title = "Window", width = 800, height = 600,
                 flags = glfw.OPENGL_PROFILE | glfw.OPENGL_DEBUG_CONTEXT,
                 visible = True, resizable = True):
        self._glfw_window = None
        self._glfw_callback_dict = dict()
        self._glfw_mouse_button_callback_dict = dict()
        self.title = title
        self.width = width
        self.height = height
        self.flags = flags
        self.visible = visible
        self.resizable = resizable
        self.cursor_mode = glfw.CURSOR_NORMAL
        self.cursor_position = (0, 0)
        self._context = None
        self._create_window()

    def __del__(self):
        if self._glfw_window is not None:
            glfw.destroy_window(self._glfw_window)
