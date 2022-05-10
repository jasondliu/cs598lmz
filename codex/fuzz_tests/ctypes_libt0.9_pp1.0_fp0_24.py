import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


# Downloading 3 Libraries from PyPI
# pyttsx3, pipwin and pyobjc-core
# NOTE: If the libraries are already downloaded, skip to next step
import pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Pyttsx3 is a Python library to convert Text to Speech
install("pyttsx3")
# PyObjC depends on PyObjC-Core
install("pyobjc-core")
# PIPWIN is a library which will help use pre-build binaries of Package which is not supported on PyPI and to install the same
install("pipwin")
# Now we download pyobjc-framework-Cocoa package which will give us a Cocoa API for Python
pipwin.install("pyobjc-framework-Cocoa")
# Now import the installed packages

