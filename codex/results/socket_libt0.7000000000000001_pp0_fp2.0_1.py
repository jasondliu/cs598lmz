import socket
import os
import config
import hashlib

"""
the class will be used to listen to the channel
"""

class Channel:
    def __init__(self, channel_number):
        self.channel_number = channel_number
        self.port = config.PORT_LISTEN_CHANNEL[channel_number]
        self.channel_name = config.CHANNEL_NAME_LIST[channel_number]
        self.channel_log_file = config.CHANNEL_LOG_FILE[channel_number]
        self.channel_vod_file = config.CHANNEL_VOD_FILE[channel_number]

    def listen(self):
        if os.path.exists(self.channel_log_file):
            os.remove(self.channel_log_file)
        if os.path.exists(self.channel_vod_file):
            os.remove(self.channel_vod_file)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("127.0
