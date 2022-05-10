import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# change the file name to the name of the file you want to open
fileName = 'dictionary.txt'

# open the file
with open(fileName, 'r') as file:
    # read the file
    lines = file.readlines()
    # close the file
    file.close()

# split the lines on the comma
for i in range(len(lines)):
    lines[i] = lines[i].split(',')

# create a dictionary of the words and definitions
dictionary = {}

# add the words and definitions to the dictionary
for i in range(len(lines)):
    dictionary[lines[i][0]] = lines[i][1]

# print the dictionary
print(dictionary)

# get the word from the user
word = input('Enter a word: ')

# check if the word is in the dictionary
if word in dictionary:
    # print the definition
    print(dictionary[word])

