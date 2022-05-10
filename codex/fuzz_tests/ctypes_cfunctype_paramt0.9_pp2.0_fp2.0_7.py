import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class c_Optimizer(object):
    def __init__(self, module):
        assert module is not None
        self.dev = ctypes.c_void_p(None)
        init_method = module.get_global_method("###_init")
        init_method(ctypes.c_void_p(id(self)), ctypes.byref(self.dev))

        
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.dev is not None:
            del_method = torch.ops.get_method("###_del")
            del_method(self.dev)


    
    def step(self):
        step_method = torch.ops.get_method("###_step")
        step_method(self.dev)
        return 


    
    def add_parameters(self, **kwargs):
        add_parameters_method = torch.ops.get_method("###_add_parameters")
        self
