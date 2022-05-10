import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main(args):
    rospy.init_node('robot_interface')
    robot = RobotInterface()
    while not rospy.is_shutdown():
        robot.update()
        rospy.sleep(rospy.Duration(0.01))

if __name__ == '__main__':
    main(sys.argv)
