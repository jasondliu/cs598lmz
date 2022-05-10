import ctypes
import ctypes.util
import threading
import sqlite3
import requests
import sys
import os
import time
import subprocess
import random
import logging
import logging.handlers

def createConfig():
    """Create a configuration file using @createCFGui() if it does not exist."""
    if not os.path.isfile(CONFIG_PATH):
        logging.debug('Configuration file not found, creating new one.')
        createCFGui()

def createCFGui():
    """
    Create the configuration file @CONFIG_PATH and the dock icon which can be used to access a GUI used to configure the addon.
    """
    o = file(os.path.join(os.environ['HOME'] + '/Library/Scripts/subCon/subCon_Config.scpt'), 'w')
    o.write(dockScript)
    o.close()
    logging.debug('Dock icon created.')

    f = open(CONFIG_PATH, 'w')
    for key in configDict.keys():
        f.write(key + '=' + configDict[key] + '\n')
    f
