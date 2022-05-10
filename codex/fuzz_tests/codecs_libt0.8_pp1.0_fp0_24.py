import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
sys.stdin = codecs.getreader('utf-8')(sys.stdin.buffer)

baseURL = "https://vndb.org/v607/characters/"
startPage = 5
lastPage = 7
globalChars = {}

#get all character names from text file
with open("allCharacters_v607.txt", "r") as myfile:
	chars = myfile.readlines()

#strip all \n from lines
chars = [x.strip() for x in chars]

#get all the urls to characters
for i in chars:
	name = i.split("|", 1)[0]
	name = name.replace(" ", "_")
	name = name.replace("(", "%28")
	name = name.replace(")", "%29")
	url = baseURL + name
	global
