#!/usr/bin/env python 
# The above line is to make the python script a stand-alone executable so that when compiling you don't have to prefix the keyword python
import rospy # Import the python library for ROS
from std_msgs.msg import String # import the data type String from std_msgs

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10) # Creating an instance of a publisher using this function, where chatter is the name of the topic being published, having data type String
	rospy.init_node('talker', anonymous=True) # We are using this function to tell ROS that this python script will be a node (called talker)
	rate = rospy.Rate(10) # rate of loopping is 10Hz (kept constant)
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time() # text that will be published followed by the time stamp
		pub.publish(hello_str) # pub is the instance created on top, in which the string to be printed is passed as the arguement (hello_str)
		rate.sleep()		# keep rate of publishing constant 

if __name__=='__main__': # main loop in which the user defined function called talker, which is the node that publishes data is called 
	try: 
		talker()	# function call 
	except rospy.ROSInterruptException:
		pass 
