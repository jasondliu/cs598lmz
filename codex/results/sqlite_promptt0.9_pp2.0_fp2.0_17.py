import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# DMX
import time
from dmxlib import DmxLibrary, DmxFixture, DmxFixtureTypes, DmxFixtureAddress, DmxFixtures, DmxFixtureArchetypes
from dmxlib import DmxOutput, DmxOutputTypes, logger, b3_log_levels, b3_log_debug, b3_log_info, b3_log_warning, b3_log_error
import dmx_dumps
import dmx_bridge


# functions



# main

# Set up the library
b3_log_set_level(b3_log_debug)

# Set up the DMX output
output = DmxOutputTypes.DmxOutputSerial(dmx_bridge.DmxBridge(), "/dev/ttyDMXFSUSB2")

# Create a fixture
#Creates a fixture from scratch.
fixture = DmxFixture(DmxFixtures.CHAUVET_O_CLOCK)
#Creates a fixture by duplicating archetype fixture
#fixture = DmxFixture(DmxFixtures.
