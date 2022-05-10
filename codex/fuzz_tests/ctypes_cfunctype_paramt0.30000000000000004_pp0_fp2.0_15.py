import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def _on_mouse_event(event, x, y, flags, param):
    """
    Process mouse event.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button down at ({}, {})".format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print("Left button up at ({}, {})".format(x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right button down at ({}, {})".format(x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        print("Right button up at ({}, {})".format(x, y))
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("Middle button down at ({}, {})".format(x, y))
    elif event == cv2
