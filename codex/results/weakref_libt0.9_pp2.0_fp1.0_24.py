import weakref

from ikpy.chain import Chain
from ikpy import utils


class InverseKinematics:
    """
    InverseKinematics is a class dedicated to handle all the inverse kinematics
    calculations. It creates a simulation environment and uses the ikpy library
    to simulate events and calculate the relative positions of the objects.
    """

    def __init__(self, robot_description=None, urdf_file=None,
                 moveit_group=None):
        """
        Load the robot parameters, chain definition and chain limits
        and instantiate a chain in ikpy.
        """
        # Load the robot description
        if robot_description is None and urdf_file is None:
            robot_description = rospy.get_param('/robot_description')
            urdf_file = rospy.get_param('/robot_description')

        # This is a feeble way to get the chain name.
        self.chain_name = rospy.get_param(
                '/move_group/capabilities/'.split('/')
