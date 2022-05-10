import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

class pyHeaviside(object):
    def __init__(self,lbpf_dict={},fn=None):
        self.k_ = lbpf_dict.get('k')
        self.lbpf_dict = lbpf_dict
        if fn is None:
            raise ValueError('Function not found')
        #self.basis_fun = lbpf_dict.get('basis_fun')
        self.basis_fun = fn
        self.fun_dict = {}
        
    def __call__(self,x):
        y = 0.0
        for idx in range(self.k_):
            y += self.fun_dict[idx](x)
        return y
    
    def get_basis_fn(self,idx):
        if self.fun_dict.get(idx) is None:
            cur_dict = self.lbpf_dict
            a = cur_dict['a'][idx]
            b = cur_dict['b'][idx]
