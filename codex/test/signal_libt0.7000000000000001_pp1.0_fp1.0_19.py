import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import re

class data_read:

  def __init__(self, in_file_name):
    self.in_file_name = in_file_name
    self.data_dict = {}

  def parse_file(self):
    with open(self.in_file_name) as f:
      for line in f:
        new_word = re.match(r'\w+', line)
        if new_word:
          self.data_dict[int(new_word.group(0))] = int(line.split()[1])
    f.close()

  def get_dict(self):
    return self.data_dict

class data_write:

  def __init__(self, out_file_name):
    self.out_file_name = out_file_name

