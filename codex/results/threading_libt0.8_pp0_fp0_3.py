import threading
threading.stack_size(67108864)

class Box:
    def __init__(self, id=0, x=0, y=0, w=0, h=0, c=0, p=-1):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.p = p

    def __str__(self):
        return "%d %d %d %d %d %d %d"%(self.id, self.x, self.y, self.w, self.h, self.c, self.p)

# Read boxes from file
# Format: id x y w h c parent
def readBoxes(filename):
    with open(filename) as infile:
        lines = infile.readlines()
        boxes = []
        for line in lines:
            line = line.split(' ')
            if len(line) > 1:
                boxes.append(Box(int(line[0]), int(line[
