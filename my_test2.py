#=================================
# Basic script to connect to PX4 and read mavlink messages.
# Author: Hongyun Elliot Lee
# Date: 11/29/22
#=================================
from pymavlink import mavutil
from wakeup import wakeup

wakeup()

# set the dialect
mavutil.set_dialect("ubicoders_msgs")
# create mavserial
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')


ubicoders_msg = the_connection.mav.ubicoders_custom_encode(23, 0)
print("ubicoders_msg")
print(ubicoders_msg)
the_connection.mav.send(ubicoders_msg)

count = 0
while count < 10**5:
    attitude = the_connection.recv_match(type='ATTITUDE') # 30
    if attitude is not None:
        print(attitude)
    scaled_imu = the_connection.recv_match(type="SCALED_IMU") # 26
    if scaled_imu is not None:
        print(scaled_imu)
    new_msg = the_connection.recv_match(type='UBICODERS_CUSTOM') # 299
    if new_msg is not None:
        print(new_msg)

    count += 1

