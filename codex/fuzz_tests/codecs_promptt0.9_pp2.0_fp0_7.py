import codecs
# Test codecs.register_error
import os
# Amnesia's specific imports
import config
# static
_ = lambda x : x


# Paths
basedir = os.path.dirname(__file__)
data_folder = basedir + "/data/"
app_folder = data_folder + "applications/"
cache_folder = data_folder + "cache/"

print("base dir:", basedir)

# Create the data/ directory at first run, if it does not exist
if not os.path.isdir(data_folder):
    os.makedirs(data_folder)
    print("Created directory:", data_folder)

if not os.path.isdir(app_folder):
    os.makedirs(app_folder)
    print("Created directory:", app_folder)

if not os.path.isdir(cache_folder):
    os.makedirs(cache_folder)
    print("Created directory:", cache_folder)

# Set up config
config.setup_config()

# Font constants

# Base font for app
FONT_APP =
