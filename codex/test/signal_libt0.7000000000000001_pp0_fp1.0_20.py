import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class dv3d_scalar_field(dv3d.dv3d_base):
    def __init__(self, parent=None, gv=None):
        dv3d.dv3d_base.__init__(self)
        self.parent = parent
        self.gv = gv
        self.vars = None
        self.sf = None
        self.switch = None
        self.name = 'scalar'
        self.vars3d = None
        self.sfUV = None

    def start_data(self, datatype):
        self.vars = None
        self.sf = None
        self.switch = None
        self.vars3d = None
        self.sfUV = None

    def end_data(self):
        if not self.vars3d:
            self.parent.datawc_y1 = 1e20
