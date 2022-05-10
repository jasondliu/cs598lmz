import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)

def cb(x, y, button):
    print('click at ' + str(x) + ' ' + str(y) + ' ' + str(button))

cb_type = FUNTYPE(cb)

sdl2.SDL_AddEventWatch(cb_type, None)

# event loop
running = True
while running:
    e = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(e)):
        if e.type == sdl2.SDL_QUIT:
            running = False
            break
        elif e.type == sdl2.SDL_MOUSEBUTTONDOWN:
            pass
        else:
            pass
    else:
        pass
</code>


A:

I have an answer, but it's not pretty. The reason for the delay is that SDL2 is waiting for the event loop to finish before it can process the event. This is
