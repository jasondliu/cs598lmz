import socket,ConfigParser
from binascii import hexlify
from hashlib import md5
from urllib import quote,unquote
import urllib2
import  os,sys
import random
from time import time
from error import XiamiError
import struct
from constants import headers,XIAMI_SERVICE_URL,XIAMI_URL,format_s
from song import  Song
from album import Album
from artist import Artist
from playlist import Playlist
from user import User
#CONFIG FILE

def get_small_filepath(path):
    return path[path.rfind('/')+1:]

def get_small_title(title):
    return title [:title.rfind('.')]

CONFIG_FILE = get_small_filepath(__file__)[:-3]

def get_config(config_file=CONFIG_FILE):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    return config

def get_lfs_sig(method,url):
    lfs = get_config().get('lf
