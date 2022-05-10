import _struct as struct
from ..utils import *
from ..exceptions import *
from .base import BaseRobot
from .encoder import Encoder
from .constants import *
from .pid import PID
from .state_machine import StateMachine, State


class Rover(BaseRobot):
    def __init__(self, i2c_bus=1, address=0x8):
        super(Rover, self).__init__(i2c_bus, address)
        self.encoder_left = Encoder(self, 'left')
        self.encoder_right = Encoder(self, 'right')
        self.pid_left = PID()
        self.pid_right = PID()
        self.state_machine = StateMachine()
        self._setup_i2c()

        self._running = True

        # setup thread
        queue_state = Queue.Queue(maxsize=0)
        thread = Thread(target=self._update, args=(queue_state,))
        thread.daemon = True
        thread.start()

