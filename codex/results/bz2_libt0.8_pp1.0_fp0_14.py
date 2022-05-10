import bz2
bz2_r = bz2.BZ2File('bz2_sam.bz2',"r")
dic_mapped = pickle.load(bz2_r)
dic_mapped

bz2_r.close()

##### write pickle
bz2_w = bz2.BZ2File('bz2_sam.bz2',"w")
pickle.dump(dic_mapped,bz2_w)
bz2_w.close()
dic_mapped = pickle.load(open("bz2_sam.bz2","rb"))
