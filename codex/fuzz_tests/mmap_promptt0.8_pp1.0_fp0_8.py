import mmap
# Test mmap.mmap.readline
with open(filename, 'rb') as f:
    memmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    #os.system('tail -n '+str(last)+' '+filename+'| head -n '+str(last-first)+' > '+filename+'.test')
    fp_out=open(filename+'.test','w')
    for x in range(first+1,last+1):
        fp_out.write(memmap.readline())
    fp_out.close()
    memmap.close()
# Compare with the correct outputs
os.system('diff '+filename+'.test output/'+filename)
