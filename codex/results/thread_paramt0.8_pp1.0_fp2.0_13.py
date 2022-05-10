import sys, threading
threading.Thread(target=lambda: argparse._sys.exit(argparse._main())).start()
import rospy
from utils.utils import Utils
from car_interface.carInterface import CarInterface
from car_interface.gazebo import Gazebo
from car_interface.racePose import RacePose
from car_interface.drive import Drive
from car_interface.scan import Scan
from car_interface.laserScan import LaserScan

class CarSystem:
    def __init__(self,nodename):
        self.utils=Utils()
        self.nodename=nodename
        self.carInterface=CarInterface(self.nodename)
        self.gazebo=Gazebo(self.nodename)
        self.racePose=RacePose(self.nodename)
        self.drive=Drive(self.nodename)
        self.scan=Scan(self.nodename)
        self.laserScan=LaserScan(self.nodename)

    def __del__(self):
        del self.gazebo

