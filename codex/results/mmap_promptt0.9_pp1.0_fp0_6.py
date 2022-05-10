import mmap
# Test mmap.mmap()
# with open('LyricsBase.txt', 'r+') as fid:
#     mm = mmap.mmap(fid.fileno(), 0) # mmap.mmap can be used to wrap a file object.
#     mm.write(b'test') # then the mm object can be used to read and write data to the file.
#     print('mm.read(4): ', mm.read(4)) # what should be printed?
#     mm.seek(0)
#     print('mm.read(60): ', mm.read(60))
#     print('mm.find(b"t"): ', mm.find(b"t"))
#     mm.seek(0)
#     print('mm.readline(): ', mm.readline())
# at the end, close the mmap will sync the mmap data to the file.
# mm.close()

#####################################################################
### Assembling MatFiles and Parsing by Lyrics
#####################################################################
songList = glob.glob('./*/*/*/*.mp3')
parse = LyricsParser(
