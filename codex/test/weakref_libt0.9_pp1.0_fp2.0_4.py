import weakref
import win32api
import sys
import uuid
# ALIASES

import dev, devices

from exceptions import hardware

__VARIABLE_COUNTER = 0

__STORE_VAR = {}
################################################################################
# %%%%%%%%%%%%%%%%%%%%%%%%%%% DEVICE CLASSES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Device(object):
    """Base class for devices"""
    
    def __init__(box, *args, **kwargs):
        box.UUID = uuid.uuid1()
        if box.type == 'nameddevice':
            box.name = box.__class__.__name__
        #if box.type == 'nameddevice':
        #    if box.name in __STORE_VAR:
        #        raise Exception('Name "{0}" is already in use'.format(box.name))
        box.active = True
        box.visible = True
        box.error_message = None
        box.device_data = {}
        box.process_data = {}
