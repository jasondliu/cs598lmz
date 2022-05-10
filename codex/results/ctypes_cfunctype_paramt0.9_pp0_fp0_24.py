import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int)
class phi(object):
    def __init__(self,type):
        if type==0:
            self.type = 0
            self.Phi = FUNTYPE(lambda k: np.exp(-k**2/10.0 + k/2.0)/k**2)
            self.dPhi = FUNTYPE(lambda k: np.exp(-k**2/10.0 + k/2.0)*(0.5*k**3 - 12*k + 20)/k**4)
        else:
            print('type','0')
            raise
            
    def __call__(self,k):
        return self.Phi(k)

    def D(self,k):
        return self.dPhi(k)

class phi2d(object):
    def __init__(self,type):
        if type==1:
            self.type = 1
            self.Phi = FUNTYPE(lambda k: k)
            self.dPhi = FUNTYPE(lambda k: 1
