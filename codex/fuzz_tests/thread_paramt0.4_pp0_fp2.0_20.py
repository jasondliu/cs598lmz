import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(['\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]+['\n'*3]*10) for i in range(50)]))).start()

# 2.
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(['\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(
