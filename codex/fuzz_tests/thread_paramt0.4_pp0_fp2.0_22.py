import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# Import the core and GUI elements of Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Import the console machinery from ipython
from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport

# Create an in-process kernel
# - use this if you want to be able to use
# both the console and gui from IPython
# without ignoring the gui
kernel_manager = QtInProcessKernelManager()
kernel_manager.start_kernel()
kernel = kernel_manager.kernel
kernel.gui = 'qt'

# kernel_manager.start_kernel(show_banner=False)
# kernel = kernel_manager.kernel
# kernel.gui = 'qt'

# kernel_client = kernel_manager.client()
# kernel_client.start_channels()

