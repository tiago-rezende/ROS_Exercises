#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, String

def callback(data):
    original_message = data.data
    rospy.loginfo("I heard %s", original_message)

    new_message = f"Hola, {original_message}"
    
    # Publica a nova mensagem
    pub.publish(new_message)

def listener():
    global pub
    rospy.init_node('node_D', anonymous=True)
    
    pub = rospy.Publisher('message_D', String, queue_size=10)  # Define o Publisher aqui
    rospy.Subscriber('message_C', String, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()

