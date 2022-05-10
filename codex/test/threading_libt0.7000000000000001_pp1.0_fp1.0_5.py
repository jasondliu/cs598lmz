import threading
threading.stack_size(2**27)
import sys
import platform
sys.setrecursionlimit(10**7)

def GetPlatform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    pass

elif _platform == "darwin":
    # MAC OS X
    pass

elif _platform == "win32":
    # Windows
    import msvcrt
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

else:
    print("Unknown platform!")
    exit(0)

from io import Bytes
