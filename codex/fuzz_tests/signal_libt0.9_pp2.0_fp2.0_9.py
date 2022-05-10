import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import bs4 # beautifulsoup4

# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import tostring
# import xml.etree.cElementTree as ET
# import lxml

# import os

# import time

import sys
# import tkMessageBox  ## Needed for python3 ( instead tkMessageBox.showinfo )
sys.path.append('file:///C:/Anaconda2/Lib/site-packages/wiki_1/')
# sys.path.append('C:/Anaconda2/Lib/site-packages/wiki_1/')
TKINTER_EXISTS = True
try:
    from Tkinter import *
    import ttk as ttk
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox
except ImportError: # Python 3
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox
    import
