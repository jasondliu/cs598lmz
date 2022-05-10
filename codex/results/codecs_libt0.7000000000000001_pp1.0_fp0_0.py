import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# settings
colors       = [color(255,0,0),color(0,255,0),color(0,0,255)]
ellipse_size = 20
padding      = 4

# write a dot on the screen
def dot(x,y,color):
    fill(color)
    ellipse(x,y,ellipse_size,ellipse_size)

# get the file contents
filepath = "C:\\Users\\(your_user_name)\\Desktop\\Oscilloscope_Test.csv"
with open(filepath,'r') as f:
    data = f.read()

# split the data into lines
data = data.split("\n")

# get the number of rows
num_rows = len(data)

# get the header row
header = data[0].split(",")

# get the number of columns
num_cols = len(header)

# get the total width
total
