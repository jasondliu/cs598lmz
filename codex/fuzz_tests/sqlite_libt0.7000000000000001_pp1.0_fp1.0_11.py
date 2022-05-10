import ctypes
import ctypes.util
import threading
import sqlite3
import queue

################################################################################
# Find/initialize the QGIS library
################################################################################

# On windows, QGIS might not be in the PATH. Try some likely locations
if os.name == 'nt':
    for loc in ['C:\\OSGeo4W\\bin', 'C:\\OSGeo4W64\\bin']:
        if os.path.exists(os.path.join(loc, 'qgis_core.dll')):
            os.environ['PATH'] = loc + ';' + os.environ['PATH']

# Load the QGIS library (expect it to be in the library search path)
qgislib = ctypes.CDLL("qgis_core")

# Initialize the library - must be called before calling any QGIS functions
qgislib.QgsApplication_initQgis()

# Get handle to QGIS main thread
mainThread = qgislib.QgsApplication_thread()

# Get some handle to the QGIS logger
qgisLogger = qgislib
