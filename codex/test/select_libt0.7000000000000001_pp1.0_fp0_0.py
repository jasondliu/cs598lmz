import select
import sys
import tty
import termios
from threading import Thread
from rx import Observer
from rx.subjects import Subject
from rx.concurrency import ThreadPoolScheduler

class KeypressObserver(Observer):
    """
    Observer that captures keypresses and emits them to subscribers
    """
    def __init__(self):
        self.f = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.f)
        self.sub = Subject()
        tty.setcbreak(self.f)
        self.sched = ThreadPoolScheduler(1)
        self.sub
