import threading
threading.stack_size(32768)

# Logging set-up
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="simulation.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)

# This is the script that runs the world.

from world import World
from world_server import WorldServer
from world_client import WorldClient
from udp_server import UDPServer
from message_types import Message, MessageTypes
from simulation_parameters import SimulationParameters

from entity import Entity
from sheep import Sheep

from random import randint
from math import sqrt

from kivy.core.window import Window

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock
from kivy.properties import ObjectProperty

from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, BooleanProperty

