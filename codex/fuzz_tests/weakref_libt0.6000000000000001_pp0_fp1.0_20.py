import weakref

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

from .rotations import quaternion_from_euler
from .tf2_utils import transform_to_kdl, transform_from_kdl
from .transform_listener import TransformListener
from .transform_listener_ros import TransformListenerROS
from .transform_manager import TransformManager
from .transform_stamped import TransformStamped as TransformStamped_

class TransformBroadcaster(object):
  """
  A class for publishing coordinate frame transform information.

  Transforms are published to the ``/tf`` topic. Messages are instances of the
  :class:`tf2_msgs.msg.tfMessage` message type.

  :class:`TransformBroadcaster` can be used much like :class:`tf.TransformBroadcaster` from
  `tf <http://wiki.ros.org/tf>`_.
  """

  def __init__(self, queue_size=100, cache_time=rospy.Duration(10)):
    """
    :param queue_size
