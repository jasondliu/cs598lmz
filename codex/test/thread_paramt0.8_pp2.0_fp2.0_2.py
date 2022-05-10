import sys, threading
threading.Thread(target=lambda: sys.stdout.write(''))

# u-(x+v)-y
# L'=x+y-2z and R'=2y-z
# u-x-y is forward
# ((u-x-y)-z)-v is backward

# (a) L=(u-x-y)-z
#     L'=x+y-2z

# (b) R=((u-x-y)-z)-v
#     R'=2y-z
#     L'=R'=x+y-2z=2y-z
#     x+y=3z
#     L=R=z

# (c) L=((u-x-y)-z)-v
#     L'=x-2z
#     R'=2y-z
#     L'=R'=x-2z=2y-z
#     x=4z-2y
#     L'=x+y-2z=4z-2y+y-2z=2z
#     L=u-x-y
