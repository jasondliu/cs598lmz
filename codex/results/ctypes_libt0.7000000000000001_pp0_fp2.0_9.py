import ctypes
ctypes.windll.user32.MessageBoxW(0, "Python is installed", "Python", 1)
"""

"""
import os
import sys

python_version = sys.version[0]

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "py-{0}".format(python_version))
if path not in sys.path:
    sys.path.insert(0, path)

from py_test import main

main()
"""

"""
import os
import sys
from time import sleep

from py_test import main

python_version = sys.version[0]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "py-{0}".format(python_version))
if path not in sys.path:
    sys.path.insert(0, path)

while True:
    try:
        main()
    except Exception as e:
        print("error", e)
    sleep(1)
"""

