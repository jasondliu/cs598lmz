import socket
import threading
import time

from registry import Registry
from sensor_service_pb2 import SensorServiceResponse
from sensor_service_pb2_grpc import SensorServiceStub

SLEEP_TIME = 4

class SensorSimulator(SensorServiceStub):
    def __init__(self, r):
        self._registry = r
        self._running = True
        self._server = threading.Thread(target=self.run)
        self._channel = grpc.insecure_channel(f"{socket.gethostbyname(socket.gethostname())}:50051")
        self._stub = SensorServiceStub(self._channel)

    def start(self):
        self._running = True
        self._server.start()

    def stop(self):
        self._running = False
        self._server.join()

    def run(self):
        while self._running:
            time.sleep(SLEEP_TIME)
            self.send_value()
            self.set_state()

    def send_value(self):
        if self._
