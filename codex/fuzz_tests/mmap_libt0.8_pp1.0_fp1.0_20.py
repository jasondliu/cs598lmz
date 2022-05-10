import mmap

DATASET_PATH = "./data/ukbench"
IMAGE_PATH = os.path.join(DATASET_PATH, "Full")

sift = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

def detect_keypoints(image, path=None):
    if image is None:
        image = cv2.imread(path, 0)
    return sift.detect(image, None)

def filter_keypoints(keypoints, image, path=None):
    if image is None:
        image = cv2.imread(path, 0)
    filtered_keypoints = []
    for k in keypoints:
        x, y = k.pt
        if x > 20 and x < image.shape[1] -
