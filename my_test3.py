from my_dialects import ubicoders_msgs

mav = ubicoders_msgs.MAVLink(None)

# get single msg object
msg_object = mav.ubicoders_custom_2_encode(15, 22, 12.1234)
print(msg_object)

# serialize the msg
bin_msg = msg_object.pack(mav)
print("Encoded Message (type of byes)")
print(bin_msg)

# the msg buf is the one we need lastly
msg_buf = msg_object.get_msgbuf()
print("Encoded Message Buffer (type of bytearray)")
print(msg_buf)

# now decode the binary(serialized) msg
new_msg_object = mav.decode(msg_buf)
print("Decoded Message")
print(new_msg_object)
print("Note that the variables in float are not exact...")