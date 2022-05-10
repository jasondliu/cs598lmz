import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def returnfunction(x,y,z):
    """
    returns a function based on x
    """

    if x == "min":
        return min
    if x == "max":
        return max
    if x == "Nor":
        return lambda x,y: x
    if x == "nOr":
        return lambda x,y: -y


def ReadinAnswers(folder,alldat,allZ,allM,names,z,m,targetz,targetm,targetname,zpos,mpos,veps,chunk_size):
    """
    Read in answers from folder and store in arrays
    """
    allZ.append([])
    allM.append([])
    alldat.
