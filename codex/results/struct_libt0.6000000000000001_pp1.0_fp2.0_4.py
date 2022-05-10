import _struct
import time

import numpy as np
import numpy.linalg as la
import numpy.random as nr
import scipy.integrate as si

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.tri as tri

import util.transform as tf
import util.plot as pt

# ==============================================================================
# -- World ---------------------------------------------------------------------
# ==============================================================================


class World(object):
    def __init__(self, ego_vehicle, other_vehicles, sensors, config):
        self.ego_vehicle = ego_vehicle
        self.other_vehicles = other_vehicles
        self.sensors = sensors
        self.config = config

        self.world = None

        self.restart()
        self.world.on_tick(hk.on_world_tick)
        self.timer = None

    def restart(self):
        self.world = client.load_world(self.config.town)

        settings = self.world.get_settings()
        settings
