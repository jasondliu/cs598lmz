import lzma
lzma_path = os.path.join(os.path.dirname(lzma.__file__), 'LICENSE')
with open(lzma_path, 'r') as lzma_file:
    lzma_license = lzma_file.read()

# Munch
import munch
munch_path = os.path.join(os.path.dirname(munch.__file__), 'LICENSE')
with open(munch_path, 'r') as munch_file:
    munch_license = munch_file.read()

# PyYaml
import yaml
yaml_path = os.path.join(os.path.dirname(yaml.__file__), 'LICENSE')
with open(yaml_path, 'r') as yaml_file:
    yaml_license = yaml_file.read()

# OpenCV
open_cv_license = """
Copyright (C) 2000-2015, Intel Corporation, all rights reserved.
Copyright (C) 2009-2011, Willow Garage Inc., all rights
