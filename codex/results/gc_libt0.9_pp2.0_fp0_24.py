import gc, weakref
import rospy

from sensor_msgs.msg import JointState

class JointMonitor(object):
    def __init__(self):
        self._topics = {}

    def watch(self, topic):
        self._topics[topic] = rospy.Subscriber(topic, JointState, self.callback)

    def unwatch(self, topic):
        w = self._topics.pop(topic)
        assert(w != None)
        print("unsubscribed")
        w.unregister()

    def callback(self, data):
        print("msg received")

    def spin(self):
        rospy.spin()

def on_delete(obj):
    print("afu")
    
if __name__ == "__main__":
    rospy.init_node("joint_monitor")
    joint_monitor = JointMonitor()
    joint_monitor.watch("joint_states")
    joint_monitor.spin()
