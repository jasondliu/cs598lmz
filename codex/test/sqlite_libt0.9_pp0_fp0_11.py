import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import *
import os

bb_player_path = "/home/ysseo/public_html/myplayer/myplayerlib/libbb_player.so.1"
player_path = "/home/ysseo/public_html/myplayer/myplayerlib/libplayer.so.1"

bbplayer = ctypes.cdll.LoadLibrary(bb_player_path)

class BB_PLAYER(ctypes.Structure):
    _fields_ = [
        ("mode", ctypes.c_int),
        ("state", ctypes.c_int),
        ("file", ctypes.c_char_p),
        ]

BB_PLAYER_init = bbplayer.BB_PLAYER_init
BB_PLAYER_init.argtypes = [ctypes.POINTER(BB_PLAYER)]

BB_PLAYER_destroy = bbplayer.BB_PLAYER_destroy
BB_PLAYER_destroy.argtypes = [ctypes.POINTER(BB_PLAYER)]

BB_PLAYER_play = bbplayer.BB
