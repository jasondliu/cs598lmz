import threading
threading.stack_size(67108864) # 64MB stack

from proto import gtfs_realtime_pb2
from flask import Flask, jsonify
import requests
import time
from datetime import datetime
from collections import defaultdict
from collections import deque
import google.protobuf
from worker import Worker
import csv
import os
import os.path


def workerPrinter(queue, outputFile):
  while (True):
    try:
      prediction = queue.popleft()
      predictionDate = prediction.date
      with open(outputFile, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([predictionDate.strftime('%Y-%m-%dT%H:%M:%SZ'), str(prediction)])
    except IndexError:
      time.sleep(1)

