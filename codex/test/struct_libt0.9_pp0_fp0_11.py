import _struct
import cache
import time
import re

class AgentHeat(MonitorHeat):
    def __init__(self, monitor):
        MonitorHeat.__init__(self, monitor)
        self.heat_map = []
