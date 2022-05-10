import bz2
# Test BZ2Decompressor on entire file

# Open and decompress the BZIP2 compressed DCM files,
#   then concatenate the VOI tables of all the files
with bz2.BZ2File('P9.dcm.bz2', 'rb') as infile:
    voi = infile.read().decode('utf8')
    voi = voi.split('\n')
    voi.pop()
    voi.pop()
    voi.pop(0)
    
    voi_data = []
    # Parse the VOI table from the DICOM file
    for line in voi:
        voi_data.append(line.split(','))
        
    voi_data[0].append('Pixel Area')
    for idx in range(1, len(voi_data)):
        voi_data[idx].append(float(voi_data[idx][2])*float(voi_data[idx][3]))
    voi_data.sort(key=lambda x: x[-1], reverse=
