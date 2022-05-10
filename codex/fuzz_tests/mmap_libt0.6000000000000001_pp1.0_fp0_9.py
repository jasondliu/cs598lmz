import mmap, os
from time import time

# Create a list of all the files in the directory

f = open("/home/pi/python_games/Pong/pong_high_scores.txt", "r+")

# use mmap to map the file object to memory
mm = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
#print(mm.readline())  # prints "Hello Python!"

# close the map
mm.close()

# close the file
f.close()

#print(mm)

#files = os.listdir(path)

#print(files)


# Open the scores file, read the scores into a list, then close the file

#scores_file = open("pong_high_scores.txt", "r")
#scores_contents = scores_file.readlines()
#scores_file.close()

#print(scores_contents)

# Get the latest score from the user and convert it to an integer

#latest_score = int
