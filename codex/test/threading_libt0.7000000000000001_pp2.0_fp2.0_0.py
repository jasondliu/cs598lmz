import threading
threading.stack_size(65000)
import serial
import io
import time

class SerialThread(threading.Thread):
    def __init__(self, mqtt_client, serial_port, baudrate,
                 publish_topic, subscribe_topic, serial_timeout=0.5):
        threading.Thread.__init__(self)
        self.mqtt_client = mqtt_client
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.publish_topic = publish_topic
        self.subscribe_topic = subscribe_topic
        self.serial_timeout = serial_timeout

    def run(self):
        self.running = True
        self.mqtt_client.loop_start()
        self.mqtt_client.subscribe(self.subscribe_topic)

        ser = serial.Serial(self.serial_port, self.baudrate, timeout=self.serial_timeout, writeTimeout=0)
