import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_double, ctypes.c_double)
def init_func(func):
    func_py = FUNTYPE(func)
    return func_py
libso(init_func)
</code>
PyQt5 (qtreactor) multiprocessing crashes the app with <code>Segmentation fault (core dumped)</code>, but only if the total threads are above 2. Calling the same function works with 2 threads, but crashes with 3 or 4 threads. Any guesses why? 
Edit:
I know it's not the usual multiprocessing not working with Qt. Based on this I suspect it's a ctypes error. However, I don't know how to debug it.  Any suggestions?

Environment:
Ubuntu 16.04 LTS
pyqt5 5.9.2
python 3.5.2

