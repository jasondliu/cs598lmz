import mmap
import sys
import struct
import subprocess
from random import randint
from time import sleep
from threading import Thread
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import c_char_p, c_double, c_int


class Worker(Process):
    def __init__(self, i, n_processes, n_iter, n_values, result, lock, array):
        super(Worker, self).__init__()
        self.i = i
        self.n_processes = n_processes
        self.n_iter = n_iter
        self.n_values = n_values
        self.result = result
        self.lock = lock
        self.array = array

    def run(self):
        for i in range(self.n_iter):
            self.lock.acquire()
            self.result.value += (i + self.i) % self.n_processes
            self.lock.release()
            sleep(0.01)
        self.array[
