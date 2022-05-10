import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# initialize the display window
win = GraphWin('L-System', 800, 800)

# define the initial state, in this case a line of length 100
# and a heading of 0 degrees (up)
initial_state = Line(Point(0, 0), Point(0, 100))
initial_state.setOutline('black')
initial_state.draw(win)

# define the rules
# in this case the rules are the same for all characters
# but we could make them different if we wanted
rules = {'F': 'F+F-F-F+F', '-': '-', '+': '+'}

# define the starting string
# which is the same as the initial state
string = 'F'

# define the number of iterations
iterations = 5

# define the angle of rotation
angle = 90

# define the initial heading
# the initial heading is 0 degrees (up)
heading = 0

# define the length of the line segments
length =
