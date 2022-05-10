import codecs
codecs.register_error('strict', codecs.ignore_errors)

#For every line in the file,
#  split the line on ";" and then on ","
#  and then store the first 3 elements in an array called line
#  and then append that array to a master array called data
#Then close the file
with open("data/iris.csv") as f:
    data = [line.strip().split(";")[:3] for line in f]

#Create a new file called iris_header.csv
#Write the first line, which is the header, to this file
#  (remember, that the header is the 4th line in iris.csv)
with open("data/iris_header.csv", "w") as f:
    f.write(data[0][0] + "," + data[0][1] + "," + data[0][2] + "\n")

#For every line in the original data,
#  write the sepal length, sepal width and petal length to iris_header.csv
with open("data/iris_header.csv", "a
