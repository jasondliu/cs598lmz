import lzma
lzma.open

import ruamel.yaml as yaml
import ruamel.yaml as ryaml

# load config file
cwd = os.getcwd()
try:
    config_path = sys.argv[1]
except IndexError:
    config_path = os.path.join(cwd, "config.yaml")

with open(config_path, "r") as fid:
    config = yaml.safe_load(fid)

# load lzma compression
lzma.open

# set variables
participants = config["participants"]

raw_dir = config["raw_dir"]
derivatives_dir = config["derivatives_dir"]
group_dir = os.path.join(derivatives_dir, "group")

# read in datasets
group_ds = Dataset(os.path.join(group_dir, "group_cifti_scaled.dscalar.nii"))
group_ds.header

# create dataset for each sub
for sub in participants.keys():
    #
