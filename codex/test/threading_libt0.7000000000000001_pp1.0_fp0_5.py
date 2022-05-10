import threading
threading.Thread(target=lambda: webbrowser.open('http://localhost:8888')).start()

import os
import sys

__file__ = os.path.abspath('')
if os.path.dirname(__file__) not in sys.path:
    sys.path.append(os.path.dirname(__file__))

from notebook.notebookapp import main
main()
 
# This should open a new browser tab with a Jupyter notebook.
# You can use the tree view to navigate to our sample notebooks
# within the `notebooks` subdirectory.
