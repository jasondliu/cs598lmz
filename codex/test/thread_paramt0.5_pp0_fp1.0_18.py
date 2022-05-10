import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# This is the robot class. It contains all of the functionality of the robot
# including movement, sensors, and the neural network.
class Robot:

    def __init__(self, x, y):
        # The x and y coordinates of the robot.
        self.x = x
        self.y = y

        # The direction the robot is facing.
        self.direction = 0

        # The neural net that controls the robot.
        self.net = NeuralNetwork([5, 10, 10, 4])

        # The sensors on the robot.
