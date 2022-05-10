import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

"""
This is the main file for the DripDrop application.
"""

import os, sys, traceback, logging, logging.handlers, platform, time
import optparse
import threading

import wx
import wx.xrc
import wx.html
import wx.lib.hyperlink
import wx.lib.masked
import wx.richtext
import wx.lib.newevent
import wx.lib.agw.flatnotebook as fnb
import wx.dataview as dv

import dripdrop.lib.app
import dripdrop.lib.gui
import dripdrop.lib.gui.config
import dripdrop.lib.gui.channel
import dripdrop.lib.gui.channel_list
import dripdrop.lib.gui.channel_list_frame
import dripdrop.lib.gui.message_list
import dripdrop.lib.gui.message_list_frame
import dripdrop.lib.gui.message_log
import dripdrop.lib.gui.message
