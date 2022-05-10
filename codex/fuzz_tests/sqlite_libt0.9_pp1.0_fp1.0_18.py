import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os

class FireDepartment(object):
    """The FireDepartment class provides methods to interact with DBUS.  
    FireDepartment monitors / investigates the DBUS events of interest,
    and makes callbacks as well as report. FireDepartemnt will report 
    an alert when it detects that registered domain does not have a proper
    service (Alert).
    
    Attributes:
        name: Name of the deanonmous FireDepartment object
        dbus_system_bus: this variable will contain connection to the DBUS.
        dbus_objects: Dictionary where keys are db object names and values are registered \
        callbacks. If a call back is registered to a dbus object (with name = key) then it\
        will be called when the dbus event of interest appears. \
        Next, initialize the dbus user bus.
        domain: Domain to be investigated. 
        domains_repo_dir: Directory where the domains repo is located
        domains_repo_name: Name of the domains repo.

    """
    wakeup_time = 1
    wakeup_time_add_
