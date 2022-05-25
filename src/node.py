import rospy
from std_msgs.msg import String

class Node(object):

    def __init__(self):
        self._pub = rospy.Publisher('foo', String, queue_size=10)
        self._sub = rospy.Subscriber('foo', String, self.__callback)
        self._count = 0

        rospy.init_node('boilerplate')

        while not rospy.is_shutdown():
            self.__spin_once()
            rospy.sleep(0.5)

    def __callback(self, msg):
        rospy.loginfo('Received {}'.format(msg.data))

    def __spin_once(self):
        self._count += 1
        self._pub.publish('Hello world #{}'.format(self._count))
