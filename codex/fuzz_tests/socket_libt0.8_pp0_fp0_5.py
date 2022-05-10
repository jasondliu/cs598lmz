import socket
import subprocess
import os
import sys
import datetime
import shutil
import argparse
import uuid
import yaml
import json
import requests

from psutil import *
from threading import Thread
from time import sleep
from uuid import getnode as get_mac

#
#    TODOS
#
#    [X] allow the user to specify the io-types to use during the experiment
#    [X] allow the user to signal the benchmarking tool that the experiment has ended
#        * signal to the benchmarking tool that the benchmark has completed (the tool needs to be able to tell the difference
#    [X] allow the user to specify the foreground IO tool to use as well as the background IO tool
#    [X] allow the user to specify the time for the foreground IO tool to run
#    [X] allow the user to specify the rates for the background IO tool to run (rates for foreground tool will be hardcoded)
#    [X] allow the user to specify the number of background IO streams to execute
#    [X] allow the user to specify the size of the files to use for the IO
