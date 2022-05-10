import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
import gtk
import gobject

# import gtk.gdk as gdk
# gdk.threads_init()

# import threading

# class CallBackLoop(threading.Thread):
#     def run(self):
#         gtk.main()

# t = CallBackLoop()
# t.start()

# import time

# time.sleep(1)

# print 'ok'

# import gtk.gdk as gdk
# gdk.threads_init()

# import threading

# class CallBackLoop(threading.Thread):
#     def run(self):
#         gtk.main()

# t = CallBackLoop()
# t.start()

# import time

# time.sleep(1)

# print 'ok'

pthread = lib.pthread

_callbacks = {}

def _callback(id, value):
    _callbacks[id](value)
    return 0
