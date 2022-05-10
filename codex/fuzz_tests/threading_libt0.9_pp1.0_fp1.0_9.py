import threading
threading.stack_size(200)
import time

CHUNK_SIZE = 2048

if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0], "<device_id>")
    exit(1)

device_id= sys.argv[1]

class MySnowboyDecoder(object):
    
    def __init__(self, callbacks):
        self.detector = snowboydetect.SnowboyDetect(
            resource_filename="./resources/common.res",
            model_str="./resources/voice_trigger.umdl")
        self.detector.SetAudioGain(1)
        self.num_hotword = 0
        self.callbacks = callbacks

    def start(self):
        self.thread = threading.Thread(target=self.loop, name='snowboy loop')

    def stop(self):
        self.thread.join()
        self.thread = None

    def loop(self):
        ring_buffer = collections.deque(maxlen=self.detector.
