import _struct
+
+# nc.nc_open(str(self.nc_file_path), nc.NC_NOWRITE)
+# nc.nc_get_att_text(ncid, nc.NC_GLOBAL, 'title')
+# nc.nc_inq_dimids(ncid, True, [], [])
+# nc.nc_inq_dim(ncid, dimid, [], [])
+# nc.nc_inq_varids(ncid, [], [])
+# nc.nc_inq_var(ncid, varid, [], [], [], [])
+# nc.nc_get_var_float(ncid, varid, [])
+# nc.nc_close(ncid)
+
+
+
+
+
+class NetCDF(object):
+    def __init__(self):
+        pass
+
+    @staticmethod
+    def nc_open(nc_file_path, mode):
+        return nc.nc
