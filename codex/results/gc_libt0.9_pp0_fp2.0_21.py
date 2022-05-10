import gc, weakref
from multiprocessing import Process, Pipe
def bad_loop():
    r = [fn for fn in glob.glob('/home/vagrant/*.jpg') if
        os.path.isfile(fn)]
    for fn in r:
        img = Image.open(fn)
        compress_image(img,fn)
def good_loop():
    for fn in glob.glob('/home/vagrant/*.jpg'):
        if os.path.isfile(fn):
            img = Image.open(fn)
            compress_image(img,fn)
def compress_image(img,fn):
    img.save(fn+'.compress','JPEG')
# bad_loop()
good_loop()

# ---------------------

# child_conn.close() # closes the child file descriptor
# parent_conn.close() # closes the parent file descriptor
#
# p.join() # waits for the child process to complete
# q.join() # waits for the child process to complete
#
# s = []
# for i in range(n):
#    
