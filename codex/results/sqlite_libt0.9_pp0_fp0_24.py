import ctypes
import ctypes.util
import threading
import sqlite3
import itertools
import datetime

# using methods taken from Gammu SMSD (although stripped down quite a bit)
# so license for this file is GPL
# Copyright (c) 2002-2008 Michal Čihař
# Copyright (c) 2001 Chris Evans

#import common
#import gsm
#import tools

# Get libgammu location
#default_gammu_location = tools.FindLibGammu(tools.ALREADY_DETECTED_LIBS.get(tools.OS_WINDOWS))
#if default_gammu_location is None:
    #default_gammu_location = tools.FindLibGammu()
#libgammu = ctypes.CDLL(default_gammu_location)

libgammu_location = ctypes.util.find_library('gammu')
if libgammu_location is None:
    raise Exception('Cannot find libgammu!')
libgammu = ctypes.CDLL(libgammu_location)

# ID
CFUNCTYPE(ctypes.c_int, ctypes.c_int
