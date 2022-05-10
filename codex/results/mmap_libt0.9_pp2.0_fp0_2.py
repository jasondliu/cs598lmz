import mmap
import struct
import time
import random
from robot.api     import logger
from robot.libraries.BuiltIn import BuiltIn
from utils import *
#@PydevCodeAnalysisIgnore

class iwlUtils:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    
    
    __shared_state = {}
    def __init__(self):
        '''
        Constructor
        '''
        self.__dict__ = self.__shared_state
        self.sz_stats_struct = 512
        self.sz_buffer = self.sz_stats_struct + self.sz_buffer_struct
        self.struct_fmt = 'H'
        self.struct_iq_data = "H"
        self.struct_pktdump= "H"
        self.struct_events = "H"
        self.struct_aq_data = "HHBB"
        self.struct_calibration_data = "I"
        self.struct_buffer = str(self.sz_buffer) + '
