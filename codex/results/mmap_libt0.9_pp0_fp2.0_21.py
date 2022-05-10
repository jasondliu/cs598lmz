import mmap
import numpy
import time

import gtk
import numpy

from m3.toolbox import *
from m3.rt_proxy import *
from crane.crane_driver import Crane
from crane.m3_tendon_daq import TendonDaq
from cv_lab import SimpleCvLab

import calibration_labgui

class TendonDaqLab(SimpleCvLab):
    def __init__(self):
        SimpleCvLab.__init__(self,title='Tendon DAQ Lab - m3')
        self.init_cv()
        
        self.rt=M3RtProxy()
        self.rt.start()
        
        self.crane=Crane(self.rt)
        self.forcetorque = M3ForceTorque_Base(self.rt)
        self.daqs=[M3TendonDaq_Base(self.rt,i) for i in range(0,self.rt.get_num_tendon_daq())]
        self.offline_calibration=M3OfflineCalib
