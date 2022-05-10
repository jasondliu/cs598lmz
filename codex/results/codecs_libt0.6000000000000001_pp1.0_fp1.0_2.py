import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import sys

class Log_file:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "w")
        self.file.write("Start time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
    
    def log(self, log_str):
        print(log_str)
        self.file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + log_str + "\n")
        self.file.flush()
    
    def close(self):
        self.file.close()

log_file = Log_file("log.txt")

def get_time_str(time_num):
    return time.strftime("%Y-%m
