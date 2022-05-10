import bz2
bz2.decompress(compressed)
 

def saveDB(Dict):
    f = open('d.pkl', 'wb')
    pickle.dump(Dict, f)
    f.close()

def loadDB():
    f = open('d.pkl', 'rb')
    Dict = pickle.load(f)
    f.close()

def deleteDB():
    f = open('d.pkl', 'rb')
    Dict = pickle.load(f)
    f.close()
    Dict = defaultdict(dict)
    f = open('d.pkl', 'wb')
    pickle.dump(Dict, f)
    f.close()

deleteDB()
loadDB()
saveDB(current_Dict)
