#!/usr/bin/env python 
# The above line is to make the python script a stand-alone executable so that when compiling you don't have to prefix the keyword python
import rospy # Import the python library for ROS
from std_msgs.msg import String # import the data type String from std_msgs

def callback(data_rec):
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data_rec.data)
def listener():
	rospy.init_node('listener', anonymous=True) # We are using this function to tell ROS that this python script will be a node (called listener)
	rospy.Subscriber('chatter', String, callback) # Creating an instance of a subscriber using this function, where chatter is the name of the topic being subscribed, having data type String, and sending it to callback
	rospy.spin()
	
if __name__=='__main__': # main loop in which the user defined function called talker, which is the node that publishes data is called 
	try: 
		listener() 	# function call 
	except rospy.ROSInterruptException:
		pass 
