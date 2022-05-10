import _struct
import time

# Other person's library
import numpy as np
import cv2

# My library
import hardware_controller.hw_controller as hw_controller
import io_controller.io_controller as io_controller

def control_motor(ctrl_params, serial_obj):
    # Motor parameter
    motor_speed = ctrl_params['motor_speed']
    motor_direction = ctrl_params['motor_direction']
    motor_distance = ctrl_params['motor_distance']

    # Convert to float
    motor_speed = float(motor_speed)
    motor_direction = float(motor_direction)
    motor_distance = float(motor_distance)

    # Convert to int
    motor_speed = int(motor_speed)
    motor_direction = int(motor_direction)
    motor_distance = int(motor_distance)

    # Set
    hw_controller.set_motor_param(serial_obj, motor_speed, motor_direction, motor_distance)

def control_servo(ctrl
