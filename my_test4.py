#=================================
# Basic script to connect to PX4 and read mavlink messages.
# Author: Hongyun Elliot Lee
# Date: 11/29/22
#=================================

from my_dialects import ubicoders_msgs

mav = ubicoders_msgs.MAVLink(None)
#================================================================
# define a secrete for hash key
mav.signing.secret_key = bytearray(chr(42)*32, 'utf-8' )
mav.signing.link_id = 0
mav.signing.timestamp = 0
mav.signing.sign_outgoing = True
#================================================================

# get single msg object
msg_object = mav.ubicoders_custom_2_encode(14, 43,  12.34)
print("Define a new custom message")
print(msg_object)

# serialize the msg
bin_msg = msg_object.pack(mav)
print("Encoded Message (type of byes)")
print(bin_msg)

# the msg buf is the one we need lastly
msg_buf = msg_object.get_msgbuf()
print("Encoded Message Buffer (type of bytearray)")
print(msg_buf)


#================================================================
# uncomment below to put different secrete key - assume incorrect signature comes in.

# try:
#     mav.signing.secret_key = bytearray(chr(42)*31, 'utf-8' )
# finally:
#     print("*****************************")
#     print("Signin key does NOT match!!!!")
#     print("exiting ...")
#     print("*****************************")
#     exit(-1)

#================================================================

# now decode the binary(serialized) msg
new_msg_object = mav.decode(msg_buf)
print("Decoded Message")
print(new_msg_object)