import codecs
codecs.register_error('strict', codecs.ignore_errors)
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output accuracy/loss plot")
ap.add_argument("-m", "--model", type=str, default="cnn_model.h5",
	help="path to output trained model")
args = vars(ap.parse_args())


# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# loop over the input images
count = 0
for imagePath in imagePaths:

	# load the image, pre-process it, and store it in the data list
	
