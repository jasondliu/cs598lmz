import _struct

from apyros.metalog import MetaLog, disable_vy_logger


class Joystick(object):
    def __init__(self, name):
        self.name = name


class DrivingMode(Enum):
    MANUAL = 1
    SMART = 2


class Command(object):
    def __init__(self, mode=DrivingMode.MANUAL,
                 linear_speed=0.0, angular_speed=0.0, extra=None):
        self.mode = mode
        self.linear_speed = linear_speed
        self.angular_speed = angular_speed
        self.extra = extra

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        setattr(self, item, value)

    def __repr__(self):
        return str(self.__dict__)


class NonStopJoystick(object):
    def __init__(self):
        self.running = True

    def run(self):
        while self.
