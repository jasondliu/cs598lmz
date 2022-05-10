import threading
# Test threading daemon
from threading import Thread
from threading import Event
import time
from time import sleep

from .config import *
from .models import *
from .utils import *
from .mqtt_client import *


class Sensor(Thread):
    def __init__(self, sensor, mqtt_client, parent_logger):
        Thread.__init__(self)
        self.sensor = sensor
        self.mqtt_client = mqtt_client
        self.logger = parent_logger.getChild(self.sensor.name)

    def run(self):
        self.logger.info("Started")
        while True:
            try:
                if self.sensor.type == SensorType.DHT22:
                    self.read_dht22()
                elif self.sensor.type == SensorType.DS18B20:
                    self.read_ds18b20()
                elif self.sensor.type == SensorType.BMP180:
                    self.read_bmp180()
                elif self.sensor.type
