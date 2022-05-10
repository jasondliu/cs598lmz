import sys, threading
threading.Thread(target=lambda:sys.stdout.write("threading.Thread\n")).start()

#multiprocessing
from multiprocessing import Process
Process(target=lambda:sys.stdout.write("multiprocessing.Process\n")).start()

#subprocess
import subprocess
subprocess.Popen("echo subprocess.Popen", shell=True)

#os
import os
os.system('echo os.system')

#sys
import sys
sys.stdout.write("sys.stdout.write\n")

#celery
from celery.task.control import broadcast
broadcast('echo celery.task.control.broadcast')

#rpyc
from rpyc.utils.server import ThreadedServer
def f(conn):
    conn.root.namespace["sys"].stdout.write("rpyc.utils.server.ThreadedServer\n")
