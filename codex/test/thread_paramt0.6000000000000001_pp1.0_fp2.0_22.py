import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\r\033[K" + "=" * (int(time.time() * 3 % 40)))).start()

import os, sys, urllib2, re, time, io, binascii, json, subprocess, threading, glob, string
from datetime import datetime
import xml.etree.ElementTree as ET
import xml.sax.saxutils
import socket, struct
import httplib, urlparse

import xbmc, xbmcaddon, xbmcvfs, xbmcgui, xbmcplugin

ADDON = xbmcaddon.Addon(id='script.module.thesportsdb')
ADDON_PATH = ADDON.getAddonInfo("path").decode("utf-8")

LIB_PATH = xbmc.translatePath( os.path.join( ADDON_PATH, 'resources', 'lib' ).encode("utf-8") ).decode("utf-8")
sys.path.append (LIB_PATH)

import utils

