import bz2
bz2file = bz2file + '.bz2'
outfile = bz2file + '.out'
# open the file with 'rb' binary mode
bz2file = bz2.BZ2File(bz2file,'rb')
# write 'bz2' file data to 'out' file in binary
outfile = open(outfile,'wb')
# write the content to 'out' file
outfile.writelines(bz2file)
# close both files
bz2file.close()
outfile.close()
</code>


A:

The only reason I can think of that overwriting the file with a decompressed version of itself would not work is if there are file permissions preventing the file from being altered. In this case, the solution is to do the decompression in a temporary file, and then replace the original with the expanded version afterwards.
Here is how you could do that:
<code>with open(filename + '.bz2', "rb") as f_in:
    with open(filename + '.bz2.tmp', "wb") as f_out:
       
