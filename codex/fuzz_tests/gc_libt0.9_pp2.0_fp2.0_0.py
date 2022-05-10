import gc, weakref

gc.set_debug(gc.DEBUG_LEAK) #1



#------------------------------------------------------------------------------

def on_finalize(*args):

print('on_finalize:', args)

w.on_finalize = [on_finalize] #2



#------------------------------------------------------------------------------

def my_callback():

print('my_callback', w)

w.on_timer = [my_callback] #3



#------------------------------------------------------------------------------

def main():

queue = multiprocessing.Queue()



# Launch a process passing the queue as argument

p = multiprocessing.Process(target=monitor_process, args=(queue,))

p.start()



global w

w = wx.App(False) #4



# if this first wx.CallAfter is removed, finalize is not called again

# (but it was called at least once)

wx.CallAfter(p.is_alive) #5



for i in range(500): #6

# Workaround for #3

if not wx
