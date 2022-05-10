import weakref

from . import common, constants


class Conductor(common.BaseConductor):

    def __init__(self, bus, bus_name):
        super().__init__(bus, bus_name, constants.SERVICE_NAME)
        self.miner_bus_names = set()
        self.wakeup_sources = set()
        self.timer = None
        self.alarm = None
        self.suspended = False
        self.should_suspend = False

    def _on_miner_registered(self, bus_name):
        self.miner_bus_names.add(bus_name)
        if not self.suspended:
            self._schedule_wakeup()

    def _on_miner_unregistered(self, bus_name):
        self.miner_bus_names.discard(bus_name)
        if not self.suspended:
            self._schedule_wakeup()

    def _on_wakeup_registered(self, bus_name):
        self.wakeup_sources.add(bus_name)
