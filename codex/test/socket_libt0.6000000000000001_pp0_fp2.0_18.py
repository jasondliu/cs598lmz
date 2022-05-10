import socket
import cv2
import numpy as np
import sys
import time
import os

# MQTT
import paho.mqtt.client as mqtt

# Kafka
from kafka import KafkaProducer
from kafka.errors import KafkaError

# OpenCV
import cv2

# Zbar
import zbar

# Serial port
import serial

# Image stream
import io

# JSON
import json

# Base64
import base64

# Digi-Key API
import requests

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

