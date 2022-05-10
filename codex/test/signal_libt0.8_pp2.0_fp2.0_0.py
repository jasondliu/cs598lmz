import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt4 import QtGui, QtCore, QtSvg, uic

from std_msgs.msg import String

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

from std_srvs.srv import Empty

from user_interfaces.base_interface import BaseUserInterface


class GoToPoseUI(BaseUserInterface):

    def __init__(self, parent=None):
        super(GoToPoseUI, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.ui = uic.loadUi(os.path.join(self._resources_path, "go_to_pose_ui.ui"), self)
        self.ui.show()

