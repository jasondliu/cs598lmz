import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds-in-python
import time
def f():
    print("hello")
while True:
    f()
    time.sleep(1)

# https://stackoverflow.com/questions/16853957/how-to-get-the-current-time-in-python
import datetime
print(datetime.datetime.now())

# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
import yaml
with open("test.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)

# https://stackoverflow.com/questions/927
