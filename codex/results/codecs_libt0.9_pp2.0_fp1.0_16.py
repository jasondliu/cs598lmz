import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#f=open('C:/Users/Barenzhi/Desktop/aclImdb/aclImdb/test/labeledBow.feat')
#for i in range(1,4):
#    for i in range(8):
#        line=f.readline()
#        print(i+1,line)



#pathTrainPos="C:/Users/Barenzhi/Desktop/aclImdb/aclImdb/train/pos"
#pathTrainNeg="C:/Users/Barenzhi/Desktop/aclImdb/aclImdb/train/neg"

#pathTestPos="C:/Users/Barenzhi/Desktop/aclImdb/aclImdb/test/pos"
#pathTestNeg="C:/Users/Barenzhi/Desktop/aclImdb/aclImdb/test/neg"


#pathTrainPos="../aclImdb/train/pos"
#pathTrainNeg="../aclImdb/train/neg"
#
