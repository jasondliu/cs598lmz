import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
# get dpi
import ctypes
user32 = ctypes.windll.user32
scrnSzX = user32.GetSystemMetrics(0)
scrnSzY = user32.GetSystemMetrics(1)
print(scrnSzX)
print(scrnSzY)

# retrive sizes
with open('size.data','rb') as f:
    (h,w,dpix,dpiy)=pickle.load(f)

# multiply for dpi
h,w,dpix,dpiy=h*scrnSzX/1080,w*scrnSzY/1080,dpix*scrnSzX/1080,dpiy*scrnSzY/1080

# restore ratios
h=h*0.9
w=w*0.8

# places
import os
path=os.getcwd().replace('\\','/')

# ready variables
character=tk.StringVar(frame_left)
character.set('None')

