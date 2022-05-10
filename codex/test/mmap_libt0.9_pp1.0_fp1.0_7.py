import mmap
import math
from ProgressBar import ProgressBar



def isInt(i):
    try:
        int(i)
    except ValueError:
        return False
    return True


