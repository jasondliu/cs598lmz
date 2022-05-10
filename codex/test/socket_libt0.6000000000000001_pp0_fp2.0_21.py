import socket
import time
import json
import time

from hal.cameras.base import CameraBase
from hal.network.connection import Connection
from hal.network.messages import MessageType, Message, FrameMessage


class Camera(CameraBase):
    """
    Camera class
    """

    def __init__(self, camera_id, host_name, port, camera_type, camera_name, image_width, image_height):
        """
        Initializes a camera

        :param camera_id: Camera ID
        :param host_name: Host name
        :param port: Port
        :param camera_type: Camera type
        :param camera_name: Camera name
        :param image_width: Image width
        :param image_height: Image height
        """
        super().__init__(camera_id, host_name, port, camera_type, camera_name, image_width, image_height)

        self.connection = Connection(host_name, port)
        self.connection.connect()

