import bz2
bz2.decompress(bz2_dat)
 
#1e-2 times the size of the original
#in this case, it is a lossless compression
#however, we can usually find lossy compressions that compress better
print('Length of compressed string: %d' % len(bz2_dat))
 
#multiprocessing
# by just doing this, you can use 4 cores to run the same code, which is really good
# of course, you need to tell it how to split the data into 4 chunks

num_cores = multiprocessing.cpu_count()
print('Number of cores: %d' % num_cores)
 
def sum_product(a,b):
    return (a+b)*(a*b)
 
def process_one(x):
    return sum_product(x,x)
 
def process_all(nums):
    pool = multiprocessing.Pool(processes=num_cores)
    result=pool.map(process_one,nums)
    pool.close()
    pool.
