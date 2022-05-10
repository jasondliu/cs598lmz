import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p)

print("Importing PyEDFlib")
import PyEDFlib
print("PyEDFlib imported")

class Test(object):

    def __init__(self):
        # PyEDFlib
        self.EDF = PyEDFlib.Edfreader(self.filename)
        if self.EDF.signals == 0:
            print("PyEDFlib: no signals in EDF file, exiting")
            sys.exit(1)
        else:
            print("PyEDFlib: EDF file contains %i signals" % self.EDF.signals)
        self.channels = []
        for i in range(self.EDF.signals):
        	self.channels.append(self.EDF.getSignalHeader(i))
        self.srate = round(self.ED
