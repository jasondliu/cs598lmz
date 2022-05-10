import socket
import time
import struct
import numpy as np
import math
import tf
import rplidar as rp
import messages_robocup_ssl_wrapper_pb2
import packet_pb2


class RoboCupRplidar():
    """
    Wrapper class around the RoboCup rplidar
    """

    def __init__(self, host, port=20011):
        """
        Constructor
        """
        self._num_points = 361
        self._host = host
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # connect to the socket
        self._sock.connect((host, port))
        self._stamp = rospy.Time.now().to_nsec()
        self._angle_inc = np.deg2rad(1)
        self._scan_angle = np.arange(-np.pi, np.pi + self._angle_inc, self._angle_inc)

    def stop(self):
        self._s
