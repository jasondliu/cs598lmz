import ctypes
ctypes.cast(0, ctypes.py_object).value = None
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# Suppress verbose information error messages

# Global parameters
batch_size = 100
image_size = 32
img_size_flat = image_size * image_size
img_shape = (image_size, image_size)
num_channels = 1
num_classes = 4
val_acc = 0.0

def load_data(dirname="data"):
    images = []
    labels = []
    
    # Loop through the folders in the directory
    for label_name in os.listdir("{}/{}".format(dirname, dirname)):
        # Loop through the images in the folder
        for image_name in os.listdir("{}/{}/{}".format(dirname, dirname, label_name)):
            # Read the image
            img = imageio.imread("{}/{}/{}/{}".format(dirname, dirname, label_name
