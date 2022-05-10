import sys, threading

def run(): #runs in thread
    for i in range(1000):
        print("hello world")

threading.Thread(target=run).start()

#new thread for executing pygame
threading.Thread(target=lambda: pygame.display.set_mode((400, 300))).start()

# Make sure the main thread quits.
while True:
    pass
</code>
Output:
<code>hello world
hello world
hello world
hello world
hello world
hello world
...
[12597:17358:0610/224625:ERROR:gl_surface_glx.cc(837)] GLX 1.3 or later is required.
[12597:17358:0610/224625:ERROR:gl_initializer_x11.cc(157)] GLSurfaceGLX::InitializeOneOff failed.
hello world
hello world
hello world
hello world
hello world
</code>
...

