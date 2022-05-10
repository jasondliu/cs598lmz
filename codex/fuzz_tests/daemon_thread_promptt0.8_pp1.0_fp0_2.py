import threading
# Test threading daemon
import time
# Test command
import unittest
# Test command
import shutil
# Convert time stamp
import time
# Parse HTML
import re
# Parse HTML
from HTMLParser import HTMLParser
import filecmp
# Site directory
from siteconf import *
# Site scripts
from scriptconf import *
# Site objects
from siteobj import *

#==============================================================================
# Site class
class Site:
    """Site class"""
    #==========================================================================
    # Constructor
    def __init__(self, name, directory, scripts, objects):
        """Constructor"""
        # Set name
        self.name = name
        # Set directory
        self.directory = directory
        # Set scripts
        self.scripts = scripts
        # Set objects
        self.objects = objects
        # Set rendered files
        self.rendered = {}
        # Set last timestampt
        self.last_timestamp = 0
    #==========================================================================
    # Render the site
    def render(self):
        """Render the site"""
        # Change directory
        os.chdir(self.
