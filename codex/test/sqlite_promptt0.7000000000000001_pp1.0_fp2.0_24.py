import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/db/systemstats/stats.db", detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)

#
# Utility methods
#

def get_all_sensors():
    """
    Returns a dict of all the sensors that can be monitored. The dictionary is
    keyed by the sensor's name and the value is a tuple of the sensor's
    identifier and the sensor's type.
    """
    sensors = {}
    sensor_id = 0

    while True:
        try:
            sensor_info = systemstats.get_sensor_info(sensor_id)
        except IndexError:
            break
        
        sensors[sensor_info.name] = (sensor_id, sensor_info.sensor_type)

        sensor_id += 1

    return sensors

def lookup_sensor(sensors, sensor_name):
    """
    Returns the identifier and type of the specified sensor. If a sensor isn't
    found, a KeyError exception is raised.
    """
