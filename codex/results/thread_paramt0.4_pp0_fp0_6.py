import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection

from pydrake.all import (
    AddMultibodyPlantSceneGraph, DiagramBuilder, Parser, PlanarSceneGraphVisualizer,
    Simulator, SignalLogger, VectorSystem,
)
from pydrake.examples.pendulum import PendulumPlant
from pydrake.geometry import ConnectDrakeVisualizer
from pydrake.multibody.plant import MultibodyPlant
from pydrake.multibody.parsing import Parser
from pydrake.systems.analysis import Simulator
from pydrake.systems.framework import DiagramBuilder
from pydrake.systems.meshcat_visualizer import MeshcatVisualizer
from pydrake.systems.rendering import PoseBundle
from pydrake.
