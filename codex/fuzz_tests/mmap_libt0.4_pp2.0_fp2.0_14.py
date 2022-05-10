import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers
from metahandler import metacontainers

# Enable metahandlers
metaget = metahandlers.MetaData(preparezip=False)

# Enable SimpleDownloader
downloader = SimpleDownloader()

# Enable addon
addon = Addon('plugin.video.filmon.tv', sys.argv)

# Enable net
net = Net()

# Enable localization
_ = addon.getLocalizedString

# Set addon info
__addonname__   = addon.getAddonInfo('name')
__addonid__     = addon.getAddonInfo('id')
__addonversion__= addon.getAddonInfo('version')
__addonpath__   = addon.getAddonInfo('path
