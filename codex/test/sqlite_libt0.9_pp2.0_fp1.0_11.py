import ctypes
import ctypes.util
import threading
import sqlite3
from peewee import *
import logging
from threading import Thread
import time
from store import SqliteDataBase
from store import PeeweeDataBase
from store import PostgreSQLDatabase
from store import ModelToDict
import json
from pymavlink import mavutil

from requestor import RequestWrapper, RequestBigDictionary, RequestSmallDictionary, RequestHome, RequestTemperatures, RequestStatus, RequestSoarings, RequestPilot
from requestor import MutexRequestHandle
from responseHander import SimpleFetcher, JSONRequestHandler, ImageFetcher, ClockFetcher, HomeFetcher, TempsFetcher, StatusFetcher, SoaringsFetcher, PilotFetcher

from config import Config

from hawkthreads import GliderProcess, PhoenixProcess, EasyParseProcess, APRSProcess, UtilProcess

from http.server import HTTPServer, CGIHTTPRequestHandler

class HWServer(Thread):
    def __init__(self, arg_HW_server):
        self._HW_server = arg_HW_server
        Thread.__
