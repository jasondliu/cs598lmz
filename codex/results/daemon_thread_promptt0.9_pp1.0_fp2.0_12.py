import threading
# Test threading daemonic
from sys import exit
import time

from lab_well_plate_parser import *
from lab_automation_tools import *
#from lab_plate_absorbance_reader import * #OLD VERSION
from lab_plate_absorbance_reader_hummingbird import *
from lab_serial_devices import *
from lab_geardrivers import *
from lab_led_controller import *


def checkProgramRefresh(PR):
    """
    run last after the program is finished
    to check if the program has been refreshed,
    if so start over again
    @param PR: boolean on program refresh
    @return: Update PR
    """
    if PR:
        return True
    else:
        return False


class StopProgram(threading.Thread):
    """
    class to stop the program using a key press
    """

    def __init__(self, stop_event):
        super(StopProgram, self).__init__()
        self.stopped = stop_event

    def run(self):
        while not self.stopped.wait(0.
