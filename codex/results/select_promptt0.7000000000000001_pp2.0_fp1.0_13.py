import select
# Test select.select()
# I added this in because I wasn't sure if you had select() on windows
# and if you didn't have it on windows we'd have to write a function
# to simulate it.

# This program is going to open two pipes, one to send data to send_data
# and another to receive data from send_data.  It will then use select()
# to monitor each pipe for readable data.  If there is data to read, it will
# read it, print it and then echo it back to send_data.

# I wrote send_data.c to implement this program.
# The command line for the program is:
# send_data <number of messages> <number of charcters in each message>

# For example, I run it with:
# send_data.exe 10 40

# This causes it to send 10 messages, each containing 40 characters.

# test_select.py is the python program that receives the data.

# When I run it, I get output that looks like this:
# $ python test_select.py
# writeFD:  3
# readFD: 
