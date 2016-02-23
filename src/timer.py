#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time

class Timer:
  def __init__(self):
    self.start = time.time()

  def restart(self):
    self.start = time.time()

  def get_time_hhmmss(self):
    end = time.time()
    m, s = divmod(end - self.start, 60)
    h, m = divmod(m, 60)
    time_str = "%02d:%02d:%02d" % (h, m, s)
    return time_str

def talker():
    rospy.init_node("timer_node", anonymous=True)
    timer_pub = rospy.Publisher("timer", String, queue_size=10)
    timeElapsed = Timer()
    while not rospy.is_shutdown():
        time = timeElapsed.get_time_hhmmss()
        timer_pub.publish(time)



if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
