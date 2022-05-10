import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong()
    y = ctypes.c_ulong()

def getMousePosition():
    pt = S()
    windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt

def getMousePosition0():
    return {'x':getMousePosition().x, 'y':getMousePosition().y}

def setMousePosition(x,y):
    x = int(x)
    y = int(y)
    ctypes.windll.user32.SetCursorPos(x, y)

def setMousePosition0(pos):
    x = pos['x']
    y = pos['y']
    ctypes.windll.user32.SetCursorPos(x, y)

class Mouse:
    def __init__(self):
        pass

    def get_position(self):
        return getMousePosition0()

    def set_position(self, x, y):
        setMousePosition(x, y)

