import mmap

import pcbnew
import re
import functools
import struct

import sys
sys.path.append('/usr/lib/python3/dist-packages')

from decimal import *
getcontext().prec = 4

n_tolerance = 3

class FootprintWizardPlugin( pcbnew.ActionPlugin ):
    """
    A script to generate a power connector footprint
    How to use (example):
        Start pcbnew
        Go to Preferences > Configure Paths and add the path to this script to the PYTHONPLUGINPATH
        Go back to the Pcbnew window and select Tools > External Plugins > Footprint Wizard
    """
    def defaults( self ):
        self.name = "Footprint Wizard"
        self.category = "Footprint Wizard"
        self.description = "A wizard to create footprints"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'screw.png')
        self.show_toolbar_button = True

    def Run( self ):
        dialog = Foot
