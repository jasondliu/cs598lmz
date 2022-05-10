import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

################################################################################
# create a new window

win = graphics.GraphWin("My Window",500,500)
win.setCoords(0,0,100,100)

################################################################################
# create a polygon

poly = graphics.Polygon(graphics.Point(10,10),graphics.Point(20,30),graphics.Point(40,25))
poly.setFill("red")
poly.draw(win)

################################################################################
# create a rectangle

rect = graphics.Rectangle(graphics.Point(50,40),graphics.Point(75,70))
rect.setFill("blue")
rect.draw(win)

################################################################################
# create a line

line = graphics.Line(graphics.Point(80,80),graphics.Point(90,90))
line.setOutline("black")
line.setWidth(2)
line.draw(win)

################################################################################
# create a circle

circ = graphics.Circle(graphics.Point(75
