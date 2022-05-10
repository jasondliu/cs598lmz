import mmap
# Test mmap.mmap zero copy feature
# We need to add a header like :
# typedef struct {
#    UINT32    ImageSize;
#    UINT32    ImageNum;
#    UINT32    AllocMode;
#    UINT32    LoopParam;
#    UINT32    ImageLen[ImageMaxNum];
# }ImageParam_t;

# So, we need to set these 5 parameters in the uint32 list.

# NvMedia Worker
# Read 4 bytes each time.
# Check 0x45454545 == EEEE to find header
# Get parameters
# Check if ImageNum is bigger than 3 and ImageSize is between 0 and 16384
# Check length and calculate total length
# Check next poi == EEEE and then check mode and length
# Image[0] is the index of images
# Image[1] is the parameter table
# Image[2] is the length data
#
# Read from offset 4
# 4 * 11 = 44 = 0x2C

# ############################################################################
#  FUNCTIONS - START
# ############################################################################


def testm
