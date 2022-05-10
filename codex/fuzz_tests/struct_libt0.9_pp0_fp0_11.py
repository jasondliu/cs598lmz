import _struct
import cache
import time
import re

class AgentHeat(MonitorHeat):
    def __init__(self, monitor):
        MonitorHeat.__init__(self, monitor)
        self.heat_map = []
        print 'aagent heat init'
        for z in range(self.monitor.system.get_zplane()):
            self.heat_map.append([])
            for i in range(self.monitor.system.get_x_max()):
                self.heat_map[z].append([])
                for j in range(self.monitor.system.get_y_max()):
                    self.heat_map[z][i].append( 0 )

    def stop(self):
       pass

    def reset(self):
        self.heat_map = []
        for z in range(self.monitor.system.get_zplane()):
            self.heat_map.append([])
            for i in range(self.monitor.system.get_x_max()):
                self.heat_map[z].append([])
                for j in range(
