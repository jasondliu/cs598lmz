from _struct import Struct
s = Struct.__new__(Struct)
file = open('The_Bear,_the_Dolls,_and_the_King.txt', 'r')
content = file.read()
content_lst = content.split()

s.delimiter = '0'
s.pack_into = lambda a,b,c,d: None

