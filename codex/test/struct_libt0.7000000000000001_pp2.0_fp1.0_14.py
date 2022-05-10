import _struct

from gps.lib.logWriter import LogWriter
from gps.lib.formats.nmea import nmeaChecksum
from gps.lib.gpxWriter import GPXWriter
from gps.lib.dedupe import GpsDedupe
from gps.lib.serialManager import GPSSerial
from gps.lib.gpsConfig  import GPSConfig
from gps.lib.gpsMath    import GpsMath
from gps.lib.gpsCache   import GpsCache

#-------------------------------------------------------------------------------
# Class C:
#  Process GPX file and store data in the database
#-------------------------------------------------------------------------------
class GPXProcessor(object):
    def __init__(self, options, cache, gpxFile=None):
        self.__options = options
        self.__cache = cache
        self.__gpx = None
        self.__gpxFile = gpxFile
        self.__log = LogWriter()
        self.__gpxFile = gpxFile
        self.__gpxData = None

