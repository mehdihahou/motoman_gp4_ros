#!/usr/bin/env python2
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("Move_programme_Mehdi_Uchiwa",anonymous=True)
robot= moveit_commander.RobotCommander()
scene=moveit_commander.PlanningSceneInterface()
group_name='manipulator'
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher= rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

#we can get the name of the reference frame from this robot:
planning_frame = group.get_planning_frame()
print('==========Reference frame: %s'% planning_frame)

#we can also print the name of the end-effector link for this group:
eef_link= group.get_end_effector_link()
print('================End effector: %s' % eef_link)

#we can get a list of all the groups in the robot:
group_names= robot.get_group_names()
print("============= Robot Groups: %s"%group_names)

#we can get the robot states:
print('================================')
print(robot.get_current_state())
print("================================")

# # We can get the joint values from the group and adjust some of the values:
joint_goal = group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = 0
joint_goal[2] = 0
joint_goal[3] = 0
joint_goal[4] = 0
joint_goal[5] = 0


# # The go command can be called with joint values, poses, or without any
# # parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)


# #Planning to a Pose Goal
# pose_goal = geometry_msgs.msg.Pose()
# pose_goal.orientation.w = 0
# pose_goal.position.x = 0
# pose_goal.position.y = 0
# pose_goal.position.z = 0
# group.set_pose_target(pose_goal)

# # #Now, we call the planner to compute the plan and execute it.
# plan = group.go(wait=True)