import socket
import threading
import uuid

#ROS Imports
import rospy
import std_msgs
import geometry_msgs

#User Imports
import xbox_node.msg

# Global Variables
host = '192.168.1.3'
port = 12000
address = (host,port)

# This linearizes the data from the xbox 360 controller and publishes them.
def main():
    main_socket = create_socket()

    """
    Each broker creates a new publisher. All publishers must share the same
    message type, but can have different topic names.
    """
    xbox_pub = rospy.Publisher("xbox_broadcaster", xbox_node.msg.xbox_data, queue_size = 100)
    rospy.init_node("xbox_360_node", anonymous = False)
    rate  = rospy.Rate(25)

    while not rospy.is_shutdown():
        xbox_data = read_data()

        """
        We create a message object, and fill it with data from the
