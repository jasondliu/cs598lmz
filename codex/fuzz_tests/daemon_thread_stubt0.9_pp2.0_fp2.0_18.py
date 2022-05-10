import sys, threading

def run():
    sys.path.append("/home/hadoop/contrib/cloudyr/amazonline/")
    sys.path.append("/home/hadoop/contrib/cloudyr/amazonline/templates/")
    from amazonline import app as application

threading.Thread(target=run).start()

# dosylayla veya textBox ile verileri transfer ediyoruz
myFile=open("/home/hadoop/contrib/cloudyr/amazonline/veriler.txt", "r")
myText=myFile.read().split("\n")
myFile.close()

# verileri parseliyoruz
for i in range(len(myText)):
    myText[i]=myText[i].split("\t")
    if "." in myText[i][0]:
        myText[i][0]=float(myText[i][0])
    else:
        myText[i][0]=int(myText[i][0])
    if "." in myText[i][1]:
        my
