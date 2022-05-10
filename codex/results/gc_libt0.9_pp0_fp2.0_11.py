import gc, weakref
import string, re, os
import application, appuifw, e32
import key_codes, e32stdin
import sysinfo

# Declare this one as global so that interpreter
# can have interrupt it.
import thread, threading

# On device, GLES code paths are to be used. Workaround for PyS60 bug.
try:
    import graphics
    graphics.screendevice = graphics.SCREENSAVER
except ImportError:
    import gles as gameplay
    import eglgles as egl
else:
    import eglgldrawable as egl

import gameplay

# Wrapper to support messageloop if interpreter is put to sleep
def application_wrapper(main):
    try:
        appuifw.app.directional_pad = False
        appuifw.app.screen = 'normal'
        appuifw.app.menu = [(u"Exit", lambda: e32stdin.set_quit())]
    except ValueError:
        # Exit menu has to be added only once
        pass
    appu
