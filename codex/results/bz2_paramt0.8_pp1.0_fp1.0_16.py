from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.open(basename+'.bz2').read())

# ###############################################################################################
# #################################### Read raw binary data ######################################
# ###############################################################################################
# filin = open('output.dat','rb')
# sid = filin.read(4) # Read 4 bytes of int
# while sid != '': # Read until no more data
#       print (sid);
#       try: # Read the next n bytes
#           data = filin.read(np.fromstring(sid,dtype='int32')[0])
#           mrt = np.fromstring(data,dtype='int32')
#           print('Shape: {}, Len: {}, First: {}, Last: {}'.format(mrt.shape, len(mrt),mrt[0],mrt[-1]))
#           sid = filin.read(4) # Read 4 bytes of int
#       except:
#           break
# filin.close()
# ###############################################################################################
# #############################################################################################
