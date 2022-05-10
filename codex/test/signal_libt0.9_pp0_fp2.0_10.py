import signal
signal.signal(signal.SIGINT, get_sigint_handler)
import os
import inspect
import subprocess
import coloredlogs, logging
import threading

from .utils import util_test

inf = float("inf")

# https://stackoverflow.com/a/4825933/539470
def get_sigint_handler(signum, frame):
    print("Ctrl+C (SIGINT) caught. Exiting...")
    sys.exit(0)

def create_results_folder(results_folder_name):
    results_folder_name = os.path.abspath(os.path.expanduser(results_folder_name))
    if not os.path.exists(results_folder_name):
        os.makedirs(results_folder_name)
    return results_folder_name

def which_path(cmd):
    return subprocess.check_output(["which", cmd]).decode("utf-8").strip()

