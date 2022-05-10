import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong)

class BRASENHAM(object):
    @staticmethod
    def line(start, end):
        assert isinstance(start, (tuple, list))
        assert isinstance(end, (tuple, list))
        assert len(start)==2
        assert len(end)==2

        x1, y1 = start
        x2, y2 = end
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        ix = 0
        iy = 0
        dx = x2 - x1
        dy = y2 - y1
        cx = x1
        cy = y1
        if dx == 0:
            ix = 0
        elif dx > 0:
            ix = 1
        else:
            ix = -1

        if dy == 0:
            iy = 0
        elif dy > 0:
            iy =
