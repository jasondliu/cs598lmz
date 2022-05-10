import gc, weakref
from pydiq import utils, microscope
from threading import Thread
from wx.lib.mixins.listctrl import ColumnSorterMixin
from PIL import Image
import threading
import traceback
try:
    from pydiq.tasks.task import Task
except:
    pass

from pydiq.tasks import track
import os.path


## app = wx.PySimpleApp()
## app.MainLoop()

# ## print 'a'
# ## import sip
# ## sip.setapi('QString', 2)
# ## print 'b'
# ## import pyqtgraph

# import sys
# import sip

# print sys.version_info
# print sip.getapi('QString')
# print sip.getapi('QVariant')
# sys.exit(0)


import pyqtgraph.examples
pyqtgraph.examples.run()

# import pyqtgraph.examples
# pyqtgraph.examples.run()

# import pyqtgraph.examples
# pyqtg
