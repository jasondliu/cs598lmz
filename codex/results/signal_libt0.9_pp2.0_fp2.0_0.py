import signal
signal.signal(signal.SIGINT, signal_handler)

# rospy.spin() is necessary for this node to be able to get a new image every time.
# rospy.spin()
try:

    while not rospy.is_shutdown():
        rospy.spin()


except rospy.ROSInterruptException:
    pass
