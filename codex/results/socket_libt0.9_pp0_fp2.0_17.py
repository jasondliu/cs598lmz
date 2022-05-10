import socket, getopt, re, os, sys, pprint, logging, datetime, commands, re, socket, datetime, time
import pexpect, coloredlogs
from coloredlogs import ColoredFormatter

os.system('clear')

class log:
    def __init__(self):
        try:
            self.formatter = ColoredFormatter(
                "%(asctime)s: %(log_color)s%(levelname)-8s%(reset)s: %(log_color)s%(message)s%(reset)s",
                "%d/%m/%Y %H:%M:%S %p",
                datefmt = None,
                reset = True,
                log_colors = {
                    'NOTICE': 'cyan',

                    'DEBUG': 'blue',
                    'INFO': 'white',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bg_white',
                },
                secondary_log_colors = {},
                style = '%'
           
