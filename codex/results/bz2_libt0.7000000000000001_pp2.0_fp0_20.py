import bz2
bz2.BZ2Compressor()

def main():
    # inputs
    jobid = sys.argv[1]
    xml_file = sys.argv[2]
    xmp_file = sys.argv[3]
    dng_file = sys.argv[4]
    jpg_file = sys.argv[5]    

    jpg = open(jpg_file, 'rb').read()
    xml = open(xml_file, 'rb').read()
    xmp = open(xmp_file, 'rb').read()
    dng = open(dng_file, 'rb').read()

    # set up metadata
    meta = {}
    meta['camid'] = '1'
    meta['timestamp'] = str(int(time.time()))
    meta['imagesize'] = str(len(jpg))
    meta['xmlsize'] = str(len(xml))
    meta['xmpsize'] = str(len(xmp))
    meta['dngsize'] = str(len(dng))
    meta['jobid
