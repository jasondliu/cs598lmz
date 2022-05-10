import bz2
bz2.__file__
file = bz2.BZ2File('/home/neo/Applications/bitcoin/bitcoin-0.8.6-linux/daemon/database/blocks/rev00000.dat.bz2','r')
file.readline()
 

file.seek(0,2)
file.close()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

fname = 'try.bz2'
blocks = bz2.BZ2File(fname,'r')

minlat= 90.0
minlng= 180.0
maxlat=-90.0
maxlng=-180.0

cx = 0.0
cy = 0.0
cz = 0.0
total = 0.0

for i,block in enumerate(blocks):
    magic,blocksize,block = read_block(block)
    mrk,ver,
