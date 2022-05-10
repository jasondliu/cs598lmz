import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)


def reset(g):
    """ Resets the global state of the graphic, and uses black color"""
    global numObjects, colorIdx
    numObjects = 0
    colorIdx = 0
    g.backColor(0x0)


def nextColor(g):
    """Checks if a color is nearing the end of the list and, if yes,
    chooses a pure color. If not, go to next in the list, then return
    the color to use."""
    global colors, colorIdx, numColors
    if colors[colorIdx][0] > 0.85:
        colorIdx = (colorIdx+1)%numColors
    elif colors[colorIdx][1] > 0.85:
        colorIdx = (colorIdx+1)%numColors
    elif colors[colorIdx][2] > 0.85:
        colorIdx = (colorIdx+1)%numColors
    elif colors[colorIdx][0]+0.15 < colors[color
