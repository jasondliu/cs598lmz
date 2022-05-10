import ctypes
# Test ctypes.CFUNCTYPE
class GLFWVidMode(ctypes.Structure):
    _fields_ = [("width", ctypes.c_int),
                ("height", ctypes.c_int),
                ("redBits", ctypes.c_int),
                ("greenBits", ctypes.c_int),
                ("blueBits", ctypes.c_int),
                ("refreshRate", ctypes.c_int)]
getMonitors = glfw.glfwGetMonitors
getMonitors.restype = ctypes.POINTER(ctypes.c_void_p)
getMonitorPos = glfw.glfwGetMonitorPos
getMonitorPos.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
getMonitorPhysicalSize = glfw.glfwGetMonitorPhysicalSize
getMonitorPhysicalSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
