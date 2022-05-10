import select
import socket
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'TV Shows': [{'name': 'TV Shows',
                        'thumb': 'http://www.vidsplay.com/vids/crab.jpg',
                        'video': 'http://www.vidsplay.com/vids/crab.mp4',
                        'genre': 'Animals'},
                       {'
