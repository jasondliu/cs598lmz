import ctypes
ctypes.cdll.LoadLibrary("../../lib/libvrep.so")

import vrep

def get_position(clientID, body_handle):
    return vrep.simxGetObjectPosition(clientID, body_handle, -1, vrep.simx_opmode_blocking)

def get_orientation(clientID, body_handle):
    return vrep.simxGetObjectOrientation(clientID, body_handle, -1, vrep.simx_opmode_blocking)

def get_linear_velocity(clientID, body_handle):
    return vrep.simxGetObjectVelocity(clientID, body_handle, vrep.simx_opmode_blocking)

def set_linear_velocity(clientID, body_handle, vx, vy, vz):
    vrep.simxSetObjectFloatParameter(clientID, body_handle, 2012, vx, vrep.simx_opmode_blocking)
    vrep.simxSetObjectFloatParameter(clientID, body_handle, 2013, vy, vrep.sim
