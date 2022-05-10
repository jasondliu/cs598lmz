import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)


def stop_callback(ros_node):
    print("Stopping node %s" % ros_node.name)

    ros_node.stop()


def main():
    ros_node = rospy.init_node('mavros_node', disable_signals=True, log_level=rospy.DEBUG)
    ros_rate = rospy.Rate(50)

    rospy.on_shutdown(stop_callback, ros_node)

    drone = drone_interface()

    print("Initialized node %s" % ros_node.name)

    while not rospy.is_shutdown():
        drone.update_state()

        if drone.is_armed:
            drone.move_drone(0.0, 0.0, 0.0, 0.0)
        else:
            drone.arm_drone()

        ros_rate.sleep()


if __name__ == "__main__":
    try:
        main
