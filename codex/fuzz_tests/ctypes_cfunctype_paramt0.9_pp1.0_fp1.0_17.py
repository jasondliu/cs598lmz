import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_uint32,ctypes.c_uint32,ctypes.c_uint32)
#~ 
def sim_callback(address,writesize,value):
    #print "Simulation: %s(%08X,%08X) => %08X" % (sim_func_names[address],writesize,value)
    if (writesize,value) in sim_vals:
        print "\t".join((str(address),str(writesize),str(value),str(sim_vals[(writesize,value)])))
#~ 
sim_types[0] = FUNTYPE(sim_callback)


sim_vals = {}
sim_funcs = {}
sim_func_names = {}

class SimFuncDict(object):
    def __init__(self,f,name):
        self.f = f
        self.name = name
    def __call__(self,*args):
        retval,callback = self.f(*args)
        sim_vals[args] = retval
        sim_fun
