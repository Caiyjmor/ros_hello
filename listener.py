#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("收到消息：%s", data.data)

def listener():
    rospy.init_node('listener_node', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()