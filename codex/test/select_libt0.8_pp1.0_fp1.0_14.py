import select
import socket
import sys

from frame import frame
from random import randrange
from threading import Thread
from threading import Lock
from threading import Condition
from threading import Event
from time import ctime, sleep
import os


def print_time(thread,delay):
    count=0
    while count<5:
        sleep(delay)
        count+=1
        print( "%s : %s" %(thread,ctime(time())))

def send_message(thread):
    count=0
    while count<5:
        sleep(randrange(3))
        count+=1
        print( "%s : %s" %(thread,ctime(time())))
        s.send(b'\x01\x00abcdefghijklmnopqrstuvwxyz\x02')


def send_message_thread():
    t1=Thread(target=send_message,args=('thread-1',))
    t2=Thread(target=send_message,args=('thread-2',))
    threads.append(t1)

