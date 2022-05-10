from bz2 import BZ2Decompressor
BZ2Decompressor.decompress()

outputName = '"Output Name"'; #file the output dictionary.
outputFile = './outputFiles/' + args.output + '.npy';

#init blank input / output lists
inList = [];
outList = [];
#read in all images and resize/gray as needed
for filename in os.listdir(rawFolder):
	if ".png" in filename:
		image = imread(rawFolder + filename);
		#if this is true, images are color (i.e. have shape of 2D, not 3D)
		if(np.array(np.shape(image))[0] == 2):
			grayimage = rgb2gray(image);
			grayimage = resize(grayimage, newSize)
		else:
			grayimage = resize(image, newSize)
		if filename[0] not in outList:
			outList.append(filename[0])
			inList.append([])
		curList = inList[outList.index(filename[0])]
