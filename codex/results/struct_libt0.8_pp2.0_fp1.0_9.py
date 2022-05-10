import _struct
+from PIL import Image, ImageDraw
+from numpy.random import *
+from trueskill import *
+from trueskill.backends import cdf
+
+
+if __name__ == '__main__':
+    # Please set your own access token
+    access_token = 'YOUR_ACCESS_TOKEN'
+
+    # Initialize TrueSkill environment
+    env = TrueSkill(draw_probability=0.01)
+    # Use mu=25.0, sigma=8.333, beta=4.167, tau=0.083 for TrueSkill 2004
+    # Use mu=25.0, sigma=8.333, beta=4.167, tau=0.083 for TrueSkill 2009
+
+    # Connect to Smite API
+    smite_api = SmiteAPI(access_token)
+
+    # Get all gods
+    gods = [god['Name'].replace(' ', '').replace('.', '').replace('\'', '') for god in smite_api.get_gods
