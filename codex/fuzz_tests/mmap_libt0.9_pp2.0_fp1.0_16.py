import mmap
import array as arr
from os import listdir
from os.path import isfile, join
import scipy.io

root_path = 'D:\\Major Project\\Data\\NYU\\'
subject_list = range(1, 14)
training_subject_list = range(0, 14)

depth_map_dir = root_path + 'depth\\'
color_map_dir = root_path + 'color\\'
joint_map_dir = root_path + 'joint_data\\'

skeleton_stonehall_dir = root_path + 'skeleton\\'
skeleton_su_dir = root_path + 'skeleton_su\\'

subject = "1_1"
calib_file = root_path + 'intrinsics\\' + subject + '.txt'
color_map_file = color_map_dir + subject + '.png'
depth_map_file = depth_map_dir + subject + '.mat'
joint_map_file = join_map_dir + subject + '.mat'

color_calib = open(
