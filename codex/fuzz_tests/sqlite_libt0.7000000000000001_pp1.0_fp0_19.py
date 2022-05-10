import ctypes
import ctypes.util
import threading
import sqlite3
import time
import json
import urllib2
import math

# Globals
# TODO: Make these configurable
config = {
    'CHUNK_SIZE': 100,
    'RABBITMQ_HOST': 'localhost',
    'RABBITMQ_PORT': '5672',
    'RABBITMQ_USER': 'guest',
    'RABBITMQ_PASSWORD': 'guest',
    'RABBITMQ_QUEUE': 'requests',
    'RABBITMQ_EXCHANGE': 'exchange',
    'RABBITMQ_ROUTING_KEY': 'routing_key',
    'RABBITMQ_HEARTBEAT_INTERVAL': 300
}

def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config['RABBITMQ_HOST'], port=int(config['RABBITMQ_PORT']),
                                  credentials=pika.PlainCredentials(config['RABBITMQ_USER'],
                                                                   
