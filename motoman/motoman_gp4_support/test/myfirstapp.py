#!/user/bin/env python

from geometry_msgs.msg import Pose, Point
import math
import rospy

def show_pose():
    print(r.get_current_pose())

if __name__== "__main__":
    rospy.init_node("robot_myfirst_node")

    r=Robot(__REQUIRED_API__VERSION__)
    show_pose()