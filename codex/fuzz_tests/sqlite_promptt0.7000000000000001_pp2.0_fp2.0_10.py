import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sys
sys.path.append('..')
import libs.constantes as constantes

try:
    from libs.Sample import Sample
    from libs.Sample import SampleType
    from libs.Sample import SampleAlarm
    from libs.Sample import SampleError
except ImportError as e:
    print("Error: missing libraries, please check README.md")
    raise

# try:
#     from pydoor.libs.Sample import Sample
#     from pydoor.libs.Sample import SampleType
#     from pydoor.libs.Sample import SampleAlarm
#     from pydoor.libs.Sample import SampleError
# except ImportError as e:
#     print("Error: missing libraries, please check README.md")
#     raise

def alarm_callback(sample):
    print("[Python Callback] Received an alarm from: ", sample.device)
    print("[Python Callback] Alarm type: ", sample.type)
    print("[Python Callback] Alarm: ", sample.alarm)
