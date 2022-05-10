import threading
# Test threading daemon
from time import sleep
from random import randint
from threading import Thread
from daemon import Daemon

def thread_with_daemon():
    print "in thread_with_daemon"
    sleep(10)
    print "done sleeping"

def daemon_thread(delay, daemon):
    print "in daemon_thread"
    daemon_thread.counter += 1
    sleep(delay)
    print "counter: ", daemon_thread.counter
    print "done sleeping"
daemon_thread.counter = 0

def launch_daemon_thread(delay, daemon):
    t = Thread(target=daemon_thread, args=(delay, daemon))
    t.setDaemon(daemon)
    t.start()

def main():
    print "main"
    #launch_daemon_thread(10, False)
    #launch_daemon_thread(5, True)
    #sleep(1)
    #print "after sleep"
    #t = Thread(target=thread_with_daemon)
    #t.start()
    #print "after start"
