import weakref
from IPython.core import ipapi, Pretty
from IPython.core.macro import Macro, macro


if hasattr(os, 'getcwd'):
    os_getcwd = os.getcwd
else:
    os_getcwd = os.getcwdu

if hasattr(os, "name") and os.name == 'nt':
    os_name = 'win'
elif hasattr(os, "name") and os.name == 'os2':
    os_name = 'win'
else:
    os_name = 'unix'

if os_name == 'win':
    from win32com.shell import shell, shellcon
    
    # for some reason, the win32com package *sometimes* gives an error
    # we don't know why, thus the try-except
