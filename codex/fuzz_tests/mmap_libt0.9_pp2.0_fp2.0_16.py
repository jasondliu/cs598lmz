import mmap
import sys
from itertools import count
from tqdm import tqdm
sys.path.append('/home/yangwang/Chinese_re-ranking/data')
sys.path.append('/home/yanshuo/xdivision_harder_blocks/tools')
from rc4_decrypt import rc4_decrypt

cnt  = 0

for f in os.listdir('/home/yangwang/Chinese_re-ranking/data_original/'):
    if '醫學' in f:
        sys.exit(0)
os.makedirs('/home/yangwang/Chinese_re-ranking/data/醫學')
os.makedirs('/home/yangwang/yanshuo_test/test_old/醫學')
os.system('rm -r /home/yangwang/yanshuo_test/test/醫學')
os.system('cp /home/yangwang/Chinese_re-ranking/data_original/醫學 /home/yangwang/yans
