import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

from pymavlink import mavutil
import droneapi.lib, droneapi.module

__all__ = ['get_distance_longlat', 'get_bearing_longlat',
           'get_location_metres', 'get_location_metres_from_latlon',
           'get_distance_metres', 'get_bearing_metres',
           'sim_map', 'SimMapPoint']

def get_distance_longlat(origin, destination):
    """
    Get ground distance between two points in metres longitude/latitude using
    haversine formula
    
    Parameters
    ----------
    origin: tuple: (long, lat)
    destination: tuple: (long, lat)
    
    Returns
    -------
    float
    """
    a = math.pi / 180.0
    d_lon = (destination[1] - origin[1]) * a
    d_lat = (destination[0] - origin[0]) * a
    lat1 = origin[0] * a
