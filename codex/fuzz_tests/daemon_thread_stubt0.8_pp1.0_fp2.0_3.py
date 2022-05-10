import sys, threading

def run():
    import time, os
    os.system("export LD_LIBRARY_PATH=/opt/vc/lib:")
    print("not running yet")
    sys.path.append("/home/pi/Vision/robot/")
    from robot import robot
    robot = robot(1)
    print("running")
    robot.enable()
    robot.drive(0,0)
    robot.disable()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()
</code>

