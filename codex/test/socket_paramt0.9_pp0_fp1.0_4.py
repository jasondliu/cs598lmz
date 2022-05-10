import socket
socket.if_indextoname(1)

a = apio.get_object("a")
a.extent
a.screen_get_root()

"""
    Get the ref of the mouse device
"""
def get_pointer_device():
    return apio.get_object("devPointer")

def get_keyboard_device():
    return apio.get_object("devKeyboard")

"""
    Get the position of the mouse
"""
def get_mouse_position(mouse_device = None):
    if mouse_device is None:
        mouse_device = get_pointer_device()
    return mouse_device.elem[0][2]

"""
    Move the mouse to a position (relative or absolute)
"""
def move_mouse(position, mouse_device = None, relative = False):
    if mouse_device is None:
        mouse_device = get_pointer_device()
    if relative:
        current_position = tuple(get_mouse_position(mouse_device))
        position = tuple(map(operator.add, current_position, position))
