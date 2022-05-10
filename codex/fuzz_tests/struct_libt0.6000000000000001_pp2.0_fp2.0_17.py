import _struct
import time
import pickle
import zlib

# Import the PCS library
import pcs

# Import the PCS clients
import pcs.packets.mote.mote_defines as d

class SerialPort(object):
    """
    This class implements a serial port client to connect to a mote.
    """
    
    def __init__(self,portName,baudrate):
        """
        Initialize the serial port client.
        portName:   serial port name.
        baudrate:   serial port baudrate.
        """
        
        # Store params
        self.portName   = portName
        self.baudrate   = baudrate
        
        # Local variables
        self.serialPort = None
        
    #======================== public ==========================================
    
    def open(self):
        """
        Open the serial port.
        """
        
        # open the serial port
        self.serialPort = serial.Serial(self.portName,self.baudrate)
        
        # reset the mote
        self
