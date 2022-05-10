import threading
# Test threading daemon
from time import sleep
#from enum import Enum

from multiprocessing import Process, Lock


from IOT.chatbot.GA_Chatbot import Chatbot
from IOT.chatbot.chatbot_socket import Socket
from IOT.chatbot.event_queue import Event_Queue    # For led driver
from IOT.relay.relay_driver import Relay_Driver
from IOT.camera.camera_driver import Camera_Driver
from IOT.smart_blind.blind_driver import Blind_Driver
from IOT.smart_bulb.bulb_driver import Bulb_Driver
from IOT.speech2text.speech2text import Speech2Text
from IOT.text2speech.text2speech import Text2Speech
from IOT.sensor.sensor_driver import Sensor_Driver
from IOT.sensor.sensor_monitor import Sensor_Monitor
from IOT.message_queue.message_queue import Message_Queue
from IOT.message_queue.send_receive import Send_Receive_MsgQ
from IOT.voice_recognition.voice_recognition import
