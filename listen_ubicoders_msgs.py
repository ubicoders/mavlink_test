#=================================
# Basic script to connect to PX4 and read mavlink messages.
# Author: Hongyun Elliot Lee
# Date: 11/29/22
#=================================
from pymavlink import mavutil
from wakeup import wakeup
wakeup()

mavutil.set_dialect("ubicoders_msgs")
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')
ubicoders_msg = the_connection.mav.ubicoders_custom_encode(23, 0)

# Keep reading the mavlink messages. i.e attitude and scaled imu
while True:
    #=======================================================================
    the_connection.mav.send(ubicoders_msg)
    #=======================================================================
    new_msg = the_connection.recv_match(type='UBICODERS_CUSTOM') # 299
    if new_msg is not None:
        print(new_msg)
