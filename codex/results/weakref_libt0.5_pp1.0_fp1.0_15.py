import weakref

from . import _dynamixel_io
from ._dynamixel_io import *

# This is a list of all the Dynamixel motors we have seen.
_dynamixel_motors = []

class DynamixelMotor(object):
    """A single Dynamixel motor attached to a serial port.

    This class provides a simplified interface for controlling a single
    Dynamixel motor. It is compatible with the Dynamixel AX-12A and
    MX-28 motors.

    """

    def __init__(self, serial_port, motor_id, motor_type=None,
                 timeout=0.1):
        """Create a new DynamixelMotor object.

        serial_port -- a serial.Serial object for the port that the motor
                       is attached to.
        motor_id -- the ID of the motor to control.
        motor_type -- the type of motor, either AX12A or MX28. If not
                      specified, the motor type will be read from the
                      motor itself.
        timeout -- the timeout in seconds to use for serial port
                   operations.

        """
        self._serial_port
