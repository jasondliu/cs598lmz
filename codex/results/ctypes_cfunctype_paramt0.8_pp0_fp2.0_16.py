import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    None, ctypes.c_float * 16, ctypes.c_float * 16, ctypes.c_float * 16
)


def get_view():
    view = glGetFloatv(GL_MODELVIEW_MATRIX)
    #res = glGetFloatv(GL_VIEWPORT)
    proj = glGetFloatv(GL_PROJECTION_MATRIX)
    cproj = ctypes.c_float * 16
    cview = ctypes.c_float * 16
    cres = ctypes.c_float * 16

    opengl.gl4.gl4lib.glGetFloatv(GL_MODELVIEW_MATRIX, view)
    #res = glGetFloatv(GL_VIEWPORT)
    opengl.gl4.gl4lib.glGetFloatv(GL_PROJECTION_MATRIX, proj)

    view = np.array(view.T)
    proj = np.array(proj.T)

    #get_view = FUNTYPE(opengl.gl4.gl4lib.gl
