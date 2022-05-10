from lzma import LZMADecompressor
LZMADecompressor()

# Setup the detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Load the image
img = cv2.imread(image_path)
img = imutils.resize(img, width=500)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ask the detector to find the bounding boxes of each face. The 1 in the
# second argument indicates that we should upsample the image 1 time. This
# will make everything bigger and allow us to detect more faces.
dets = detector(img, 1)

num_faces = len(dets)
if num_faces == 0:
    print("Sorry, there were no faces found in '{}'".format(image_path))
    exit()

# Find the 5 face landmarks we need to do the alignment.
faces = dlib.full_object_detections()
for detection in dets:
    faces.append(predictor(
