import threading
threading.stack_size(1024000)

from magcam_functions import *
import pdb
from pymmcore import Image, CImage, CameraList, Camera
from PYME.DSView.dsviewer import View3D

from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons
from PYME.LMVis.layers import NamedImage, RGBImage
from PYME.misc.computerName import GetComputerName
from PYME.misc.computerName import GetComputerIPAddress
from PYME.misc.AutoFoldPanel import *

from PYME.DSView.dsviewer import ViewIm3D

from PYME.LMVis import gl_render3D


if sys.version_info[0] == 2:
    import SocketServer as socketserver
    import Queue as queue
else:
    import socketserver
    import queue


def start_view():
    if 'visFr' not in dir(camview):
        visFr = wx.Frame(None, -1, size=(520,650))
        

