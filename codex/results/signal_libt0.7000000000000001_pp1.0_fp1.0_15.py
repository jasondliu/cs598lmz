import signal
signal.signal(signal.SIGINT, handler)

# Set up the connection
client = naoqi.ALProxy("ALMotion", robot_ip, robot_port)

# Get the List of Joints
JointNames = client.getBodyNames("Body")

# Set the fraction of max speed
Speed = 0.1

# Initialize the move
client.post.angleInterpolation(JointNames, JointAngles, Speed, True)

# wait is useful because with post the motion start immediately
time.sleep(3.0)

# Example showing a single joint move
#
# Set the fraction of max speed
Speed = 0.2

# Define The Initial Position
InitialPosition = -0.2

# Define The Final Position
FinalPosition = 0.2

# Go to the Initial Position
client.post.angleInterpolation(JointNames[0], InitialPosition, Speed, True)

# Go to the Fina Position
client.post.angleInterpolation(JointNames[0], FinalPosition, Speed, True)

# Go to the Initial
