import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def llcallback(i):
    print "llcallback:",i
    if i == 5:
        g_stdscr.stop_polling()
        g_stdscr.addstr(10,0,"STOPPING AND LEAVING")
        g_stdscr.refresh()
        return 1 # returning 1 is the same as break
    elif i == 10:
        g_stdscr.addstr(10,0,"poll stopping")
        g_stdscr.refresh()
        g_stdscr.stop_polling()
    else:
        g_stdscr.addstr(9,0,"poll %d%%" % (i * 10,))
        g_stdscr.refresh()
    return 0
    
    
CALLBACK = FUNTYPE(llcallback)
g_stdscr.poll(5, CALLBACK, 10)
