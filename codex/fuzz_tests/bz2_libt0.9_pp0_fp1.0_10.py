import bz2
bz2.BZ2File(out_file).seek(0)

#second step: classify the files
!$ROOT_DIR/bin/seb-Classify_segmentations $out_file $out_dir $seg_dir $label_dir

#third step: evaluate segmentations
!$ROOT_DIR/bin/seb-Evaluate_segmentations $seg_dir $label_dir $eval_dir

#and you should be ready
 

#Implementation courtesy of H. Amy Zhao, Maryam Panahiazar, and Zachary Pincus
#Licensed under the Creative Commons Attribution 4.0 (CC BY 4.0) license
#See the included LICENSE file for further information

#OTHER NOTES:
#seb-Classify_segmentations supports keras and neuralnet

%matplotlib inline
# py 4.16.14 on gray
import os
import sys
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import pickle as pkl
import pydensecrf.d
