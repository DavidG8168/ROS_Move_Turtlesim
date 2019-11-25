#!/usr/bin/env python
import rospy
import time
# Used to change the turtle's position.
from geometry_msgs.msg import Twist
# Used to get the turtle's position.
from turtlesim.msg import Pose

# This function is used to print the position of the turtle.
def callback(msg):
    # Condition used to print only when starting for the first time and stopping.
    if msg.linear_velocity == 0 and msg.angular_velocity == 0:
        # Setting the format of the printed message.
        # Print the x and y positions with 2 numbers after the decimal point.
        rospy.loginfo("(X: %.2f, Y: %.2f)" % (msg.x, msg.y))

# This function moves the turtle forward.
def move_forward():
    # The speed in the x-axis.
    msg.linear.x = 0.5
    # The current time.
    s_time = rospy.Time.now().to_sec()
    # The starting distance.
    current_distance = 0
    # While we have not passed 1 meter, keep moving.
    while current_distance <= 1:
        # Update the position by sending it throught the publisher.
        pub.publish(msg)
        # Get current time.
        f_time = rospy.Time.now().to_sec()
        # Calculate new position (x = v*t).
        current_distance = 0.5 * (f_time - s_time)
    # After the loop, stops the turtle.
    msg.linear.x = 0

# This function turns the turtle.
def change_angle():
    # Define pi.
    pi = 3.14
    # Consider the starting angel as 0.
    current_angle = 0
    # The current time.
    s_time = rospy.Time.now().to_sec()
    # The speed we will change angle at.
    turning_speed = 15 * 2 * pi / 360
    wanted_angle = 45 * 2 * pi / 360
    msg.angular.z = abs(turning_speed)
    # While we have not reached the wanted angle, keep turning.
    while current_angle < wanted_angle:
        # Update the angle by sending it through the publisher.
        pub.publish(msg)
        # Get current time.
        f_time = rospy.Time.now().to_sec()
        # Calculate new angle.
        current_angle = turning_speed * (f_time - s_time)
    # After the loop, stops the turtle.
    msg.angular.z = 0

# The main function.
if __name__ == "__main__":
    # Name the node to start so rospy can start communicating. 
    rospy.init_node("move_turtle")
    # To make the turtle move in ROS we need to publish Twist messages to the topic cmd_vel.
    # Create a publisher.
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
    # In order to print the turtle's pose we need to subscribe to the topic turtle1/pose.
    # When a new message is received , the callback function is invoked with the message as an argument.
    sub = rospy.Subscriber("turtle1/pose", Pose, callback)
    # This message has a linear component for the x,y,z velocities and an angular component for the 
    # angular rate about the x,y,z axes.
    msg = Twist()
    # Setting the rate of the of the node, approximately 10 times per second.
    rate = rospy.Rate(10)
    # Start moving.
    move_forward()
    # When done moving, turn at a 45 degree angle.
    change_angle()
    # Let the final position be printed before finishing.
    time.sleep(2)
