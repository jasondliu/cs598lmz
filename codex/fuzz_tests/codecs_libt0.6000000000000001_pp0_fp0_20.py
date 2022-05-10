import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#-------------------------------------------------------------------------------
# Import modules
#-------------------------------------------------------------------------------
import os
import sys
import getopt
import logging
import time

import numpy as np
import pandas as pd

import xml.etree.ElementTree as ET

import arcpy

from arcpy import env
from arcpy.sa import *

#-------------------------------------------------------------------------------
# Check out any necessary licenses
#-------------------------------------------------------------------------------
arcpy.CheckOutExtension("Spatial")

#-------------------------------------------------------------------------------
# Define functions
#-------------------------------------------------------------------------------
def get_XML_tree(filename):
    '''
    This function parses an XML file.
    '''
    # Parse the XML file
    tree = ET.parse(filename)
    # Get the root of the XML tree
    root = tree.getroot()
    return (tree, root)

def get_XML_root(filename):
    '''
    This function parses an XML file.
    '''
    # Parse the XML
