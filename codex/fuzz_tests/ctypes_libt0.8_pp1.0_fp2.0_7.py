import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# set paths
home = os.path.expanduser("~")
img_path = os.path.join(home, 'Desktop')
img_path = os.path.join(img_path, '{}.png'.format(name))
img_path

# get image
plt.savefig(img_path)

# open image
os.startfile(img_path)

# show image
img = mpimg.imread(img_path)
plt.figure(figsize=(10, 10))
plt.imshow(img)

# export to HTML
from IPython.display import HTML 
from IPython.display import Image

html = '<img src=\'{}\'>'.format(img_path)
HTML(html)

# closefig
plt.close()
