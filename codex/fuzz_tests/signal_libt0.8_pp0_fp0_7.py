import signal
signal.signal(signal.SIGINT, handler) # exit with keyboard interrupt

###############################################################################
#
# Load dataset
#
###############################################################################

# Loads a dataset with index and title only.
# We will use this function to extract the ids of the images.
def load_ids(name="coco_5k.pkl", path="data/"):
    ids = pickle.load(open(path + name, "rb"))
    ids = [_id[0] for _id in ids]
    print("Dataset", name, "contains", len(ids), "examples.")
    return ids

# load train/val/test splits
train_ids = load_ids("train_ids.pkl")
val_ids   = load_ids("val_ids.pkl")
test_ids  = load_ids("test_ids.pkl")


###############################################################################
#
# Data preparation
#
###############################################################################

# Load all train/val/test ids into lists
all_ids = train
