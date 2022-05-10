import socket
socket.if_indextoname(3)

#
# Using the index of the connection given by the iwconfig command,
# verify the connection is the one you want to use.
#

def get_output(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def get_iwconfig():
    cmd="iwconfig"
    output=get_output(cmd)
    return output

def find_line(input, search):
    lines=input.split("\n")
    for line in lines:
        if search in line:
            return line
    return False

def find_essid(input, essid):
    lines=input.split("\n")
    for line in lines:
        if essid in line:
            return True
    return False


network=raw_input("Enter Network Name (ESSID): ")
connection, error = get_iwconfig()

