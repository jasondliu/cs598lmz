import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Could not import matplotlib.pyplot. Please install matplotlib.")
    sys.exit(1)

try:
    import pandas as pd
except ImportError:
    print("Could not import pandas. Please install pandas.")
    sys.exit(1)

try:
    import tkinter as tk
except ImportError:
    print("Could not import tkinter. Please install tkinter.")
    sys.exit(1)

try:
    from tkinter.filedialog import askopenfilename, askdirectory
except ImportError:
    print("Could not import tkinter.filedialog. Please install tkinter.")
    sys.exit(1)

try:
    import tkinter.messagebox as tkMessageBox
except ImportError:
    print("Could not import tkinter.messagebox. Please install t
