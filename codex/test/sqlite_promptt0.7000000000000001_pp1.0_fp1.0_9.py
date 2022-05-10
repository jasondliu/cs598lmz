import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:', check_same_thread=False)

from ogr2ogr import ogr2ogr

from django.conf import settings

from geonode.geoserver.helpers import ogc_server_settings
from geonode.geoserver.signals import geoserver_pre_save_maplayer
from geonode.geoserver.signals import geoserver_post_save_maplayer

from geonode.geoserver.signals import geoserver_pre_save_map
from geonode.geoserver.signals import geoserver_post_save_map

from geonode.geoserver.signals import geoserver_pre_save_style
from geonode.geoserver.signals import geoserver_post_save_style

from geonode.geoserver.signals import geoserver_pre_save_layer
from geonode.geoserver.signals import geoserver_post_save_layer

from geonode.geoserver.signals import geoserver_
