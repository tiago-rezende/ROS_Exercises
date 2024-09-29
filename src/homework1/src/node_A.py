#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    original_message = data.data
    rospy.loginfo("I heard %s", original_message)

def listener():
    rospy.Subscriber('message_D', String, callback)

def message():
    pub = rospy.Publisher('message_A', String, queue_size=10)
    rate = rospy.Rate(0.5)  # 0.5 Hz
    msg = "Hello"
    
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('messager_A', anonymous=True)  # Inicializa o nó apenas uma vez
        listener()  # Configura o subscriber
        message()  # Envia mensagens
    except rospy.ROSInterruptException:
        pass
