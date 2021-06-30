#!/usr/bin/env python

'''

Created on Wednesday June 30
@author : Rakesh Kumar

'''

#Required Libraries
###################
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import random
import turtlesim.srv


class Catch_Bot:

    def __init__(self):
        rospy.init_node('catch_and_catch', anonymous=True)

        # Publisher - '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # Subscriber - '/turtle1/pose'.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.pose_refresh)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def main(self):
        self.Catcher()  #Calling the Catcher logic function
    

    def Catcher(self):  #Catcher logic .
        goal_pose = Pose()

        while(True):
    
            #Random Pose for spawning a turtle
            goal_pose.x=random.randrange(2,10)
            goal_pose.y=random.randrange(2,10)
            distance_tolerance=0.5  #Tolerance limit for the leader turtle (turtle1)

            #Calling spawn function to spawn a turtle in the 
            #corresponding random position
            self.Turtle_spawn(goal_pose,'turtle1','turtle2')

            vel_msg = Twist()

            while self.euclidean_distance(goal_pose) >= float(distance_tolerance):

                #Porportional controller.

                #Linear velocity in the x-axis.
                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                #Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)

                #Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)

                #Publish at the desired rate.
                self.rate.sleep()

            #Stopping our robot after the goal_location is achieved.
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)

            self.Turtle_kill('turtle2')  #Killing the turtle after it is catched

    ############################################################################
    #Supporting Functions
    #####################

    def Turtle_spawn(self,goal,killer_name,spawn_name):  #Spawn function
        self.spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
        self.turtle_name = rospy.get_param(killer_name, spawn_name)
        #Calling the /spawn service for the corresponding location
        self.spawner(goal.x, goal.y, 0, self.turtle_name) 
        #print(self.goal.x,self.goal.y)

    def Turtle_kill(self,killer_name):  #Kill function
        self.killer=rospy.ServiceProxy('kill',turtlesim.srv.Kill)
        #Calling the /kill service for the corresponding turtle
        self.killer(killer_name)

    def pose_refresh(self, data):
        #Callback function which is called when a new message of type Pose is
        #received by the subscriber.
        self.pose = data
        self.pose.x = round(self.pose.x,6)
        self.pose.y = round(self.pose.y,6)

    def euclidean_distance(self, goal_pose):
        #Euclidean distance between current pose and the goal.
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=8):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

################################################################################
#Main Program Execution
#######################

if __name__ == '__main__':
    try:
        x = Catch_Bot()
        x.main()
    except rospy.ROSInterruptException:
        pass