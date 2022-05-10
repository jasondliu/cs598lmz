import _struct
import re
import tkinter as tk
import tkinter.ttk as TTK

# enum system of status
# 0 -> title
# 1 -> mods
# 2 -> filter
# 3 -> indexes
# 4 -> inf
class Ctrl:
	def __init__(self,data,gridx=None,gridy=None,anchor=None):
		self.root = data.root
		self.data = data
		self.vars = data.vars
		self.lng = data.lng
		self.stat = data.stat
		self.gridx = gridx
		self.gridy = gridy
		self.anchor = anchor
		self.ctrl = None
	
	def set(self,tags = ["u","b","i"],fore_rgb = "000000",back_rgb = "FFFFFF",font = None,width = None,height = None,weight = None,align = None):
		"""apply tag style, foreground, background and font to ctrl 
		tags (string) default = "
