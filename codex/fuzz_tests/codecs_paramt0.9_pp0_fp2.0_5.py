import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))
import traceback
import random
random.seed(10)
import sys
import redis
import json
from crypto_aes import AESCipher

class Text_Recognizer:
    def __init__(self):
        self.ws_client = False

    def connect_rabbitmq(self):
        pass

    def connect_websocket_server(self, ip, port):
        channel = grpc.insecure_channel('%s:%s' % (ip, port))
        self.ws_client = text_recognizer.Text_RecognitionStub(channel)
        return self.ws_client

    def connect_redis(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        return r

    def send_redis(self, r, img_path, source_channel, source_channel_text):
        try:
            print("[Redis DB] Publish a new message.")
            output = source_channel_text
            text
