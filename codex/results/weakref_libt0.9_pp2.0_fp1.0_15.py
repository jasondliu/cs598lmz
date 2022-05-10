import weakref

from typing import List, Union, Optional

from wpilib.command import Command, Subsystem

from .motors import Motor


class EligibleSubsystem(Subsystem):
    
    '''
        Subsystem framework for an object that can have motors
    '''
    
    __slots__ = ('_motors', '_motor_objects')
    
    def __init__(self):
        super().__init__()
        self._motors = []  # type: List[int]
        self._motor_objects = {}  # type: Dict[int, Motor]
    
    @property
    def motors(self):
        '''
            :returns: A list of motor pids
        '''
        return self._motors
    
    def set_motors(self, *motors):
        '''
            Sets the motors of the subsystem
            :param *motors: A list of motor pids, 1 int or even Motor objects
        '''
        if len(motors) == 1 and isinstance(motors[0], (int
