import threading
threading.stack_size(1280*720*2*2)

import subprocess
import os

# script to run
script = "/home/pi/python/robot/robot.py"

# kill the python script
def kill_python():
    subprocess.call(["pkill", "python"])

# run the python script
def run_python():
    kill_python()
    subprocess.call(["python", script])

# get the last modified time of a file
def get_file_mtime(f):
    return os.stat(f).st_mtime

# file to watch for changes
watch_file = script

# get the last modified time
last_mtime = get_file_mtime(watch_file)

# run the python script
run_python()

# forever loop
while True:

    # get the current modified time
    mtime = get_file_mtime(watch_file)

    # if the modified time has changed
    if mtime != last_mtime:

        # update the last modified time
        last
