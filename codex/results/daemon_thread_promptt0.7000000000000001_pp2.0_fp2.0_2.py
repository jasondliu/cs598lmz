import threading
# Test threading daemon
#import time
#import test_daemon

# Import dbus-python
import dbus
import dbus.service
import dbus.mainloop.glib
import gobject


# Initialize gstreamer
import gst

# Import the convenience module for generating video test sources
import gst_utils

# Import the utilities for finding and loading plugins
import gst_plugin_utils

# Import the interfaces
import interfaces

#import gtk
#import logging

#global variables
global bus
global bus_name
global object_name
global test_src_list
global test_element_list
global test_sink_list
global test_pipeline_list
global test_state_list
global test_command_list
global test_playing_count
global test_paused_count

#test_src_list = []
test_src_list = []
test_element_list = []
test_sink_list = []
test_pipeline_list = []
test_state_list = []
test_command_list = []
test_playing_count
