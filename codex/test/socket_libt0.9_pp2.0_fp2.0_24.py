import socket, time, sys, threading, Queue;

class LimitSem:
    def __init__(self, capacity):
        self.capacity   = capacity;
        self.available  = capacity;
        self.lock       = threading.Lock();
        self.nonfull    = threading.Condition(self.lock);
        self.nonempty   = threading.Condition(self.lock);
    
    def acquire(self):
        self.lock.acquire();
        try:
            while self.available==0:
                self.nonempty.wait();
            self.available -= 1;
        finally:
            self.lock.release();
    
    def release(self):
        self.lock.acquire();
        try:
            self.available += 1;
            self.nonempty.notify();
        finally:
            self.lock.release();

class ZookeeperClient:
    def __init__(self, name):
        self.name   = name;
        self.lock   = threading.Lock();
        self.cond   = threading.Condition
