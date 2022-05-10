import codecs
codecs.open('C:\\Users\\sreeram\\Desktop\\py\\edureka\\fileone.txt','r','utf-8')

#print(open('C:\\Users\\sreeram\\Desktop\\py\\edureka\\fileone.txt','r','utf-8').readline())
with open('C:\\Users\\sreeram\\Desktop\\py\\edureka\\fileone.txt','r','utf-8') as f:
    print(f.read())
    
with open('C:\\Users\\sreeram\\Desktop\\py\\edureka\\fileone.txt','w','utf-8') as f:
    f.write("This is my first file\n")
    f.write("Contains second line\n")
