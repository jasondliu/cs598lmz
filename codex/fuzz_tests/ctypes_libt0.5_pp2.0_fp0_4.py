import ctypes
ctypes.windll.user32.SetProcessDPIAware()

def plot_image(image, title='Original Image'):
    plt.figure()
    plt.imshow(image)
    plt.title(title)
    plt.show()
    
def plot_histogram(image):
    plt.figure()
    plt.hist(image.ravel(), bins=256, fc='k', ec='k')
    plt.title('Histogram')
    plt.show()
    
def plot_masked_image(image, mask, title='Masked Image'):
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.imshow(mask, cmap='jet', alpha=0.5)
    plt.title(title)
    plt.show()
    
def plot_mask(mask, title='Mask'):
    plt.figure()
    plt.imshow(mask, cmap='jet')
    plt.title(title)
    plt.show()
    
