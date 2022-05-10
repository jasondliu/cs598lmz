import bz2
bz2_compressor = bz2.BZ2Compressor()

def parseData( file ):
    data = []
    userData = []
    f = gzip.open( file )
    entry = {}
    for l in f:
        cols = l.strip().split("::")
        #print cols
        if len(cols) == 1:
            continue

        if not cols[0] == '1':
            continue
        if ( cols[0] == '1' ):
            if len(userData) > 0:
                data.append( (userData[0][0],userData[0][1],userData[0][2],(int)(userData[-1][3])) )
                userData = []
        userData.append( (cols[0],cols[1],cols[2],cols[3]) )
    f.close()
    return data

def parseTxt( txtFile, outfile ):
    #filename = txtFile.split('/')[-1].split('.')[0]

