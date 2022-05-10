import _struct
+from ctypes import *
+
+### 
+### This is a script to read the PDS label files
+### associated with the Venus Cloud Profiles from
+### IRTF 2014-2015 observational campaign
+### to obtain the observational geometries used
+### for a period of high insolation state during
+### 2012-2016. This script stores the data
+### in a python dictionary that can be used to
+### put into comparison with the MODIS IR brightness
+### temperatures
+###
+
+
+# update the label file with the directory which it is in
+filename = './LBL_DATA/V08_0017255001_1.LBL'
+
+# read in the file and split into lines
+f = open(filename, "r")
+f1 = f.read()
+s = StringIO(f1)
+f_lines = s.readlines()
+
+# get rid of all the line breaks
+f_lines_br = [x.replace("\n", " ") for x in f_lines]
+
+# find
