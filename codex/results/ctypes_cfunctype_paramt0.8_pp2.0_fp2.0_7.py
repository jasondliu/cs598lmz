import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_float)
def pyfunc(arg):
    print 'called back with', arg
pycb = FUNTYPE(pyfunc)

pi.gpio_set_mode(4,4)
pi.gpio_set_pull_up_down(4,2)

pi.gpio_callback(4,4,pycb)

time.sleep(30)

pi.stop()

pi.gpio_set_pull_up_down(4,0)
